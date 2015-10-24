# Implement a simple TCP server

import socket

class Server:
    """
    Implement an extremely simple TCP server that can handle a single TCP connection
    at a time. This implementation is meant to be as stupid and as slow as possible
    to provide a worst case performance comparison against concurrent server
    implementations.
    """

    def __init__(self, port):
        self.port = port

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
            self.handle_connection(conn, addr)

    def handle_connection(self, conn, addr):
        print("Handling connection from {0}:{1}".format(addr[0], addr[1]))
        self.on_accept(conn)
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()

    def on_accept(self, conn):
        msg = "Hello.\n"
        self.write(conn, bytes(msg, 'UTF-8'))

    def write(self, conn, string):
        conn.send(string)
