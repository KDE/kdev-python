# SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>
# SPDX-License-Identifier: GPL-2.0-or-later
import socket
import threading
import struct
import os
import sys
from enum import IntEnum

# This module provides a few things:
# - kdevPdbConnection.establish() Wait for a client to connect up and initialize
# - kdevPdbConnection.sendDataFrame() Write a data frame to a peer.
# - kdevPdbConnection.getDataFrame()  Get/Wait for a data frame from a peer.
# - The received data frames are appended to a queue by the I/O thread that runs the
#   socket recv() system calls. The receive threading guarantees forward progress in
#   the case both peers send data simultaneously.
# - Sending a data frame blocks the caller until the full frame is sent.


class Stop(BaseException):
    pass


# Currently defined data-frame protocol escape codes.
class Cmd(IntEnum):
    DoNothing = 0
    Terminate = -1
    InterruptDisallowed = -2
    InterruptAllowed = -3


class kdevPdbConnection:

    def __init__(self):
        # queue of received bytes() data-frames.
        self.dataframes = []
        self.condvar = threading.Condition(threading.Lock())
        # Has recv() side of the socket been closed?
        self.stop_read = False
        # Has send() side of the socket been closed? (not guarded by condvar)
        self.stop_write = False
        self.recv_thread = None
        self.server_address = None
        self.socket = None

    def establish(self, socketpath="/tmp/"):
        """Become a server listening for a client"""
        # Initialize the IO.
        socket_addr = socketpath + "kdevpdb.socket"
        if os.path.exists(socket_addr):
            os.unlink(socket_addr)
        listensocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        if hasattr(socket, "SO_REUSEADDR"):
            listensocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listensocket.bind(socket_addr)
        self.server_address = listensocket.getsockname()
        listensocket.listen(0)
        # Print the socket file to stdout.
        # The host process must wait for "socket:" line to be printed, and discard this line.
        sys.stdout.write("socket:"+self.server_address+"\n")
        sys.stdout.flush()
        self.socket, _ = listensocket.accept()
        listensocket.close()
        self.recv_thread = threading.Thread(target=self._recv)
        self.recv_thread.start()

    def _shutdown(self, shutread, shutwrite):
        '''Shutdown the connection.
           The shutdown is done such that we send CmdTerminate first if we are fully open.
           This gives the remote peer a chance to also cleanly shutdown the connection.
        '''
        if shutwrite and not self.stop_write:
            with self.condvar:
                if not self.stop_read:
                    # the connection is fully open. Try make the remote peer shutdown cleanly.
                    self.sendCmdFrame(Cmd.Terminate)
                self.stop_write = True
                if shutread:
                    # Full shutdown, the reader side is already or will be dead.
                    self.stop_read = True
                    self.socket.shutdown(socket.SHUT_RDWR)
                    self.condvar.notify()
                    # the socket is *dead*.
                    self.socket.close()
                    self.socket = None
                    return
                # Shutdown only writer side.
                self.socket.shutdown(socket.SHUT_WR)
        elif shutread:
            # Shutdown the reader side only.
            with self.condvar:
                if not self.stop_read:
                    self.stop_read = True
                    self.socket.shutdown(socket.SHUT_RD)
                    self.condvar.notify()
                    if self.stop_write:
                        self.socket.close()
                        self.socket = None

    def _recv(self):
        '''A receiver thread that shovels data frames from the socket into the queue'''
        try:
            while True:
                blob = self._recvDataFrame()
                with self.condvar:
                    self.dataframes.append(blob)
                    self.condvar.notify()
        except Stop:
            pass
        except BaseException as e:
            print(e)
        # Close the receiving side of the socket.
        self._shutdown(True, False)

    def getDataFrame(self):
        with self.condvar:
            while not self.dataframes:
                if self.stop_read:
                    raise Stop()
                self.condvar.wait()
            return self.dataframes.pop(0)

    def stop(self):
        '''request shutdown of receiver thread and connection'''
        if self.socket is not None:
            self._shutdown(True, True)
        if self.recv_thread is not None:
            self.recv_thread.join()

    def sendCmdFrame(self, code):
        '''Send a escape code only frame'''
        assert not self.stop_write
        sendbuf = struct.pack('<i', code)
        try:
            self.socket.sendall(sendbuf)
        finally:
            pass

    def sendDataFrame(self, src):
        '''Send a frame of data'''
        sendbuf = bytearray(struct.pack('<i', len(src)) + src)
        nbytes = 0
        if self.stop_write:
            raise Stop()
        while nbytes < len(sendbuf):
            # TODO: handle any errors that we should recover from and try sending again.
            numbytes = self.socket.send(sendbuf[nbytes:])
            if numbytes > 0:
                nbytes += numbytes
            else:
                # failed to send anything, close the sending side and abort.
                self._shutdown(False, True)
                raise Stop()

    def _recvDataFrame(self):
        '''Receive a frame of data or None'''
        recv = struct.calcsize('<i')  # max length of data to receive
        # the receive buffer. Most of the frames can fit into the 4096 bytes.
        recvbuf = bytearray(4096)
        datablob = bytearray()
        bloblen = -1
        while recv > 0:
            numbytes = self.socket.recv_into(recvbuf, recv)
            if bloblen == -1 and numbytes == recv:
                # 1. got the blob length (which can be less than one for special events)
                bloblen = struct.unpack_from('<i', recvbuf, 0)[0]
                if bloblen == Cmd.DoNothing:
                    # A empty blob.
                    return None
                if bloblen == Cmd.Terminate:
                    # End the connection now.
                    raise Stop()
                if bloblen > len(recvbuf):
                    # reserve a big enough buffer..
                    recvbuf = bytearray(bloblen)
                # Ok, start receiving the payload.
                recv = bloblen
            elif bloblen > 0 and numbytes > 0:
                # 2. got some data
                datablob += recvbuf[:numbytes]
                recv -= numbytes
            else:
                # Error.
                raise Stop()
        # successfully received a data frame
        return datablob
