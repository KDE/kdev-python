class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

from QtWidgets import *

import datetime

class QX11Info():
    """"""
    def __init__(self):
        '''QX11Info QX11Info.__init__()'''
        return QX11Info()
    def connection(self):
        '''static xcb_connection_t QX11Info.connection()'''
        return xcb_connection_t()
    def display(self):
        '''static Display QX11Info.display()'''
        return Display()
    def setNextStartupId(self, id):
        '''static void QX11Info.setNextStartupId(QByteArray id)'''
    def nextStartupId(self):
        '''static QByteArray QX11Info.nextStartupId()'''
        return QByteArray()
    def getTimestamp(self):
        '''static int QX11Info.getTimestamp()'''
        return int()
    def setAppUserTime(self, time):
        '''static void QX11Info.setAppUserTime(int time)'''
    def setAppTime(self, time):
        '''static void QX11Info.setAppTime(int time)'''
    def appUserTime(self):
        '''static int QX11Info.appUserTime()'''
        return int()
    def appTime(self):
        '''static int QX11Info.appTime()'''
        return int()
    def appScreen(self):
        '''static int QX11Info.appScreen()'''
        return int()
    def appRootWindow(self, screen = None):
        '''static int QX11Info.appRootWindow(int screen = -1)'''
        return int()
    def appDpiY(self, screen = None):
        '''static int QX11Info.appDpiY(int screen = -1)'''
        return int()
    def appDpiX(self, screen = None):
        '''static int QX11Info.appDpiX(int screen = -1)'''
        return int()
    def isPlatformX11(self):
        '''static bool QX11Info.isPlatformX11()'''
        return bool()


