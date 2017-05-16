import abc
import sys


class BaseParser(object):
    def __init__(self, *args):
        try:
            self.bsoup = args.bsoup
            self.senturls = args.senturls
        except:
            print("unable to initialize properly")
            sys.exit(-1)

    @abc.abstractmethod
    def parse(self):
        pass

