"""Module "BaseHTTPServer - HTTP server base class."
    Note: the class in this module doesn't implement any HTTP request; see
    SimpleHTTPServer for simple implementations of GET, HEAD and POST
    (including CGI scripts).  It does, however, optionally implement HTTP/1.1
    persistent connections, as of version 0.3.
    
    Contents:
    
    - BaseHTTPRequestHandler: HTTP request handler base class
    - test: test function
    
    XXX To do:
    
    - log requests even later (to capture byte count)
    - log user-agent header and other interesting goodies
    - send error log to separate file"""

class BaseHTTPRequestHandler(SocketServer.StreamRequestHandler):
    """HTTP request handler base class.
    
    The following explanation of HTTP serves to guide you through the
    code as well as to expose any misunderstandings I may have about
    HTTP (so you don't need to read the code to figure out I'm wrong
    :-).
    
    HTTP (HyperText Transfer Protocol) is an extensible protocol on
    top of a reliable stream transport (e.g. TCP/IP).  The protocol
    recognizes three parts to a request:
    
    1. One line identifying the request type and path
    2. An optional set of RFC-822-style headers
    3. An optional data part
    
    The headers and data are separated by a blank line.
    
    The first line of the request has the form
    
    <command> <path> <version>
    
    where <command> is a (case-sensitive) keyword such as GET or POST,
    <path> is a string containing path information for the request,
    and <version> should be the string "HTTP/1.0" or "HTTP/1.1".
    <path> is encoded using the URL encoding scheme (using %xx to signify
    the ASCII character with hex code xx).
    
    The specification specifies that lines are separated by CRLF but
    for compatibility with the widest range of clients recommends
    servers also handle LF.  Similarly, whitespace in the request line
    is treated sensibly (allowing multiple spaces between components
    and allowing trailing whitespace).
    
    Similarly, for output, lines ought to be separated by CRLF pairs
    but most clients grok LF characters just fine.
    
    If the first line of the request has the form
    
    <command> <path>
    
    (i.e. <version> is left out) then this is assumed to be an HTTP
    0.9 request; this form has no optional headers and data part and
    the reply consists of just the data.
    
    The reply form of the HTTP 1.x protocol again has three parts:
    
    1. One line giving the response code
    2. An optional set of RFC-822-style headers
    3. The data
    
    Again, the headers and data are separated by a blank line.
    
    The response code line has the form
    
    <version> <responsecode> <responsestring>
    
    where <version> is the protocol version ("HTTP/1.0" or "HTTP/1.1"),
    <responsecode> is a 3-digit response code indicating success or
    failure of the request, and <responsestring> is an optional
    human-readable string explaining what the response code means.
    
    This server parses the request and the headers, and then calls a
    function specific to the request type (<command>).  Specifically,
    a request SPAM will be handled by a method do_SPAM().  If no
    such method exists the server sends an error response to the
    client.  If it exists, it is called with no arguments:
    
    do_SPAM()
    
    Note that the request name is case sensitive (i.e. SPAM and spam
    are different requests).
    
    The various request details are stored in instance variables:
    
    - client_address is the client IP address in the form (host,
    port);
    
    - command, path and version are the broken-down request line;
    
    - headers is an instance of mimetools.Message (or a derived
    class) containing the header information;
    
    - rfile is a file object open for reading positioned at the
    start of the optional input data part;
    
    - wfile is a file object open for writing.
    
    IT IS IMPORTANT TO ADHERE TO THE PROTOCOL FOR WRITING!
    
    The first thing to be written must be the response line.  Then
    follow 0 or more header lines, then a blank line, and then the
    actual data (if any).  The meaning of the header lines depends on
    the command executed by the server; in most cases, when data is
    returned, there should be at least one header line of the form
    
    Content-type: <type>/<subtype>
    
    where <type> and <subtype> should be registered MIME types,
    e.g. "text/html" or "text/plain"."""
    
    
    def address_string(self):    
        """
    Return the client address formatted for logging.
    
    This version looks up the full hostname using gethostbyaddr(),
    and tries to find a name that contains at least one dot."""
        
        return
    
    def date_time_string(self, timestamp=None):    
        """
    Return the current date and time formatted for a message header."""
        
        return
    
    def end_headers(self):    
        """
    Send the blank line ending the MIME headers."""
        
        return
    
    def handle(self):    
        """
    Handle multiple requests if necessary."""
        
        return
    
    def handle_one_request(self):    
        """
    Handle a single HTTP request.
    
    You normally don't need to override this method; see the class
    __doc__ string for information on how to handle specific HTTP
    commands such as GET and POST."""
        
        return
    
    def log_date_time_string(self):    
        """
    Return the current time formatted for logging."""
        
        return
    
    def log_error(self, format, *args):    
        """
    Log an error.
    
    This is called when a request cannot be fulfilled.  By
    default it passes the message on to log_message().
    
    Arguments are the same as for log_message().
    
    XXX This should go to the separate error log."""
        
        return
    
    def log_message(self, format, *args):    
        """
    Log an arbitrary message.
    
    This is used by all other logging functions.  Override
    it if you have specific logging wishes.
    
    The first argument, FORMAT, is a format string for the
    message to be logged.  If the format string contains
    any % escapes requiring parameters, they should be
    specified as subsequent arguments (it's just like
    printf!).
    
    The client host and current date/time are prefixed to
    every message."""
        
        return
    
    def log_request(self, code='-', size='-'):    
        """
    Log an accepted request.
    
    This is called by send_response()."""
        
        return
    
    def parse_request(self):    
        """
    Parse a request (internal).
    
    The request should be stored in self.raw_requestline; the results
    are in self.command, self.path, self.request_version and
    self.headers.
    
    Return True for success, False for failure; on failure, an
    error is sent back."""
        
        return
    
    def send_error(self, code, message=None):    
        """
    Send and log an error reply.
    
    Arguments are the error code, and a detailed message.
    The detailed message defaults to the short entry matching the
    response code.
    
    This sends an error response (so it must be called before any
    output has been generated), logs the error, and finally sends
    a piece of HTML explaining the error to the user."""
        
        return
    
    def send_header(self, keyword, value):    
        """
    Send a MIME header."""
        
        return
    
    def send_response(self, code, message=None):    
        """
    Send the response header and log the response code.
    
    Also send two standard headers with the server software
    version and the current date."""
        
        return
    
    def version_string(self):    
        """
    Return the server software version string."""
        
        return
    
    
    MessageClass = None
    
    default_request_version = 'HTTP/0.9'
    
    error_content_type = 'text/html'
    
    error_message_format = '<head>\n<title>Error response</title>\n</head>\n<body>\n<h1>Error response</h1>\n<p>Error code %(code)d.\n<p>Message: %(message)s.\n<p>Error code explanation: %(code)s = %(explain)s.\n</body>\n'
    
    monthname = None
    
    protocol_version = 'HTTP/1.0'
    
    responses = {100: None, 101: None, 200: None, 201: None, 202: None, 203: None, 204: None, 205: None, 206: None, 300: None, 301: None, 302: None, 303: None, 304: None, 305: None, 307: None, 400: None, 401: None, 402: None, 403: None, 404: None, 405: None, 406: None, 407: None, 408: None, 409: None, 410: None, 411: None, 412: None, 413: None, 414: None, 415: None, 416: None, 417: None, 500: None, 501: None, 502: None, 503: None, 504: None, 505: None}
    
    server_version = 'BaseHTTP/0.3'
    
    sys_version = 'Python/2.6.5'
    
    weekdayname = None
    
    
    def finish(self):    
        """
    """
        
        return
    
    def setup(self):    
        """
    """
        
        return
    
    
    rbufsize = -1
    
    wbufsize = 0
    
    
    def __init__(self, request, client_address, server):    
        """
    """
        
        return

class HTTPServer(SocketServer.TCPServer):
    """"""
    
    
    def server_bind(self):    
        """
    Override server_bind to store the server name."""
        
        return
    
    
    allow_reuse_address = 1
    
    
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):    
        """
    Constructor.  May be extended, do not override."""
        
        return
    
    def close_request(self, request):    
        """
    Called to clean up an individual request."""
        
        return
    
    def fileno(self):    
        """
    Return socket file number.
    
    Interface required by select()."""
        
        return
    
    def get_request(self):    
        """
    Get the request and client address from the socket.
    
    May be overridden."""
        
        return
    
    def server_activate(self):    
        """
    Called by constructor to activate the server.
    
    May be overridden."""
        
        return
    
    def server_close(self):    
        """
    Called to clean-up the server.
    
    May be overridden."""
        
        return
    
    
    address_family = 2
    
    request_queue_size = 5
    
    socket_type = 1
    
    
    def finish_request(self, request, client_address):    
        """
    Finish one request by instantiating RequestHandlerClass."""
        
        return
    
    def handle_error(self, request, client_address):    
        """
    Handle an error gracefully.  May be overridden.
    
    The default is to print a traceback and continue."""
        
        return
    
    def handle_request(self):    
        """
    Handle one request, possibly blocking.
    
    Respects self.timeout."""
        
        return
    
    def handle_timeout(self):    
        """
    Called if no new request arrives within self.timeout.
    
    Overridden by ForkingMixIn."""
        
        return
    
    def process_request(self, request, client_address):    
        """
    Call finish_request.
    
    Overridden by ForkingMixIn and ThreadingMixIn."""
        
        return
    
    def serve_forever(self, poll_interval=0.5):    
        """
    Handle one request at a time until shutdown.
    
    Polls for shutdown every poll_interval seconds. Ignores
    self.timeout. If you need to do periodic tasks, do them in
    another thread."""
        
        return
    
    def shutdown(self):    
        """
    Stops the serve_forever loop.
    
    Blocks until the loop has finished. This must be called while
    serve_forever() is running in another thread, or it will
    deadlock."""
        
        return
    
    def verify_request(self, request, client_address):    
        """
    Verify the request.  May be overridden.
    
    Return True if we should proceed with this request."""
        
        return
    
    
    timeout = None
__all__ = None
__version__ = '0.3'"""VERSION
    0.3"""


