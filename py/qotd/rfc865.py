class RFC865:
    """
    Blast a random quote at any unsuspecting fool that happened to connect to
    this server.
    """
    def __init__(self, tcpclass, port):
        self.tcpserver = tcpclass(port, self.handle)

    def start(self): self.tcpserver.start()
    def shutdown(self): self.tcpserver.shutdown()
    def run(self): self.tcpserver.run()

    def handle(self, conn, addr):
        msg = bytes(self.nextquote(), "UTF-8")
        conn.send(msg)

    def nextquote(self):
        return "One day this will be a randomly generated quote."

