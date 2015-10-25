import json
import random
import pprint

class Handler:
    """
    Send a random text quote to the given connection.
    """

    def __init__(self, corpus):
        self.corpus = corpus

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
