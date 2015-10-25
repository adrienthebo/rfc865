import socket
import threading

class Server:
    """
    Define a common interface for TCP servers.
    """

    def __init__(self, port, handler):
        self.port = port
        self.handler = handler

    def start(self):
        pass

    def shutdown(self):
        pass

    def run(self):
        pass

class BasicServer(Server):
    """
    Implement an extremely simple TCP server that can handle a single TCP connection
    at a time. This implementation is meant to be as stupid and as slow as possible
    to provide a worst case performance comparison against concurrent server
    implementations.
    """

    def start(self):
        """
        Initialize the listening socket.
        """
        addr = (socket.gethostname(), self.port)
        print("Listening for connections on {0}:{1}".format(addr[0], addr[1]))

        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind(addr)
        listener.listen(3)
        self.listener = listener

    def shutdown(self):
        """
        Cleanly shutdown the listening socket.
        """
        self.listener.shutdown(socket.SHUT_RDWR)
        self.listener.close()

    def run(self):
        """
        Continuously accept connections and pass connections to the on_accept handler.
        """
        while True:
            conn, addr = self.listener.accept()
            print("Handling connection from {0}:{1}".format(addr[0], addr[1]))
            self.handle_connection(conn, addr)

    def handle_connection(self, conn, addr):
        self.handler(conn, addr)
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()

class ThreadedServer(BasicServer):
    """
    Implement a TCP server that handles each connection in a separate thread.
    """

    def handle_connection(self, conn, addr):
        def func(self, conn, addr):
            print("Handling request in thread {0}".format(threading.current_thread()))
            super(ThreadedServer, self).handle_connection(conn, addr)

        thr = threading.Thread(target=func, args=(self, conn, addr))
        thr.start()
