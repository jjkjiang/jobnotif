import abc
import sys


class BaseParser(object):
    def __init__(self, bsoup, senturls, substr, t):
        self.bsoup = bsoup
        self.senturls = senturls
        self.substr = substr
        self.t = t

    @abc.abstractmethod
    def parse(self):
        pass

