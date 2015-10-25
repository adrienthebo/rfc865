import json
import random
import pprint

class Server:
    """
    Blast a random quote at any unsuspecting fool that happened to connect to
    this server.
    """
    def __init__(self, tcpclass, port):
        self.tcpserver = tcpclass(port, self.handle)
        self.corpus = read_jargon_file("./resources/jargon_file_glossary.json")

    def start(self): self.tcpserver.start()
    def shutdown(self): self.tcpserver.shutdown()
    def run(self): self.tcpserver.run()

    def handle(self, conn, addr):
        msg = bytes(self.nextquote(), "UTF-8")
        conn.send(msg)

    def nextquote(self):
        return self.corpus.random()

def read_jargon_file(path):
    o = JargonCorpus(path)
    o.read()
    return o

class JargonCorpus:
    """
    Load the Jargon file corpus and spit back random quotes from it."
    """

    def __init__(self, path):
        self.path = path
        self.document = []

    def read(self):
        try:
            fh = open(self.path, 'r')
            self.document = json.load(fh)
        finally:
            fh.close()

    def random(self):
        doc = self.document
        key = random.choice(list(doc.keys()))
        entry = {key: doc[key]}
        return json.dumps(entry) + "\n"
