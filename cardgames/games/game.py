#!/usr/bin/python3

from .. import deck
from ..log import logger
from .. import player

class Game:
    """Base class for a game.  Other classes can/should inherit from it."""
    def __init__(self, name=None, players_count=0, players_list=None):
        self.name = name

        # if players_list is not None, ensure it's the size of players_count 
        # and then add them to the list.
        # if players_list is None, create new ones.
        if players_list:
            if len(players_list) != players_count:
                logger.error('Game: bad init args')
            else:
                for player in players_list:
                    if type(player) is not player.Player:
                        logger.error('Game: player is of the incorrect type')
                    else:
                        if not self.players:
                            self.players = []
                        logger.debug('adding player')
                        self.players.append(player)
        else:
            for i in players_count:
                logger.debug('creating new player')
                if not self.players:
                    self.players = []
                self.players.append(player.Player(name='player{}'.format(str(i+1)), ptype=PlayerType.UNKNOWN, hand=None))

        #def play(self, ...)

        def __repr__(self):
            return "<Game: '{}', no players: {}>".format(self.name, str(len(self.players))

        def __str__(self, width=0):
            retstr = ''
            retstr += (width*' ') + '{}\n'.format(self.name)
            if self.players and len(self.players) > 0:
                retstr += (width*' ') + 'Players: \n'
                for p in self.players:
                    retstr += p.__str__(width=width+2)
            else:
                retstr += (width*' ') + '(No players)\n'
            return retstr

        def print(self, width=0):
            print(self.__str__(width))

