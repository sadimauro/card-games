#!/usr/bin/python3

from . import deck
from .log import logger

class Player: 
    def __init__(self, name=None, ptype=PlayerType.UNKNOWN, hand=None): 
        self.name = name
        self.ptype = ptype 
        self.hand = hand

    def __repr__(self):
        return "<Player: {}, type: {}>".format(self.name, self.ptype.__str__())

    def __str__(self, width=0):
        retstr = ''
        retstr += (width*' ') + 'Player "{}"'.format(self.name)
        if self.ptype == PlayerType.AI:
            retstr += ' (AI)'
        if self.hand:
            retstr += '; ' + self.hand.__str__()
        retstr += "\n"
        return retstr

    def print(self, width=0):
        print(self.__str__(width))

 
class PlayerType(enum.Enum): 
    UNKNOWN = 0 
    AI = 1 
    INTERACTIVE = 2 
 
    _type_dict = {UNKNOWN: 'unknown', 
            AI: 'AI', 
            INTERACTIVE: 'interactive'} 
 
    def __init__(self, type=UNKNOWN): 
        self.type = type 
 
    def __str__(self): 
        return _type_dict[self.type]    
