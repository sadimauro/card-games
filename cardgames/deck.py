#!/usr/bin/python3                                     
                                                       
import random       
               
from .log import logger
from . import utils

_suits = ['spade', 'heart', 'diamond', 'club']         
_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
_rankVals = {'A': 1,                                   
            '2': 2,                                    
            '3': 3,                                    
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 11,
            'Q': 12,
            'K': 13}
# each value is
#  (suit, rank): (suit/rank pretty-print unicode, card pretty-print unicode)
_ppCodes = {\
            ('spade', 'A'):  ('A\u2660', '\U0001F0A1'),
            ('spade', '2'):  ('2\u2660', '\U0001F0A2'),
            ('spade', '3'):  ('3\u2660', '\U0001F0A3'),
            ('spade', '4'):  ('4\u2660', '\U0001F0A4'),
            ('spade', '5'):  ('5\u2660', '\U0001F0A5'),
            ('spade', '6'):  ('6\u2660', '\U0001F0A6'),
            ('spade', '7'):  ('7\u2660', '\U0001F0A7'),
            ('spade', '8'):  ('8\u2660', '\U0001F0A8'),
            ('spade', '9'):  ('9\u2660', '\U0001F0A9'),
            ('spade', '10'): ('10\u2660', '\U0001F0AA'),
            ('spade', 'J'):  ('J\u2660', '\U0001F0AB'),
            ('spade', 'Q'):  ('Q\u2660', '\U0001F0AD'),
            ('spade', 'K'):  ('K\u2660', '\U0001F0AE'),

            ('heart', 'A'):  ('A\u2665', '\U0001F0B1'),
            ('heart', '2'):  ('2\u2665', '\U0001F0B2'),
            ('heart', '3'):  ('3\u2665', '\U0001F0B3'),
            ('heart', '4'):  ('4\u2665', '\U0001F0B4'),
            ('heart', '5'):  ('5\u2665', '\U0001F0B5'),
            ('heart', '6'):  ('6\u2665', '\U0001F0B6'),
            ('heart', '7'):  ('7\u2665', '\U0001F0B7'),
            ('heart', '8'):  ('8\u2665', '\U0001F0B8'),
            ('heart', '9'):  ('9\u2665', '\U0001F0B9'),
            ('heart', '10'): ('10\u2665', '\U0001F0BA'),
            ('heart', 'J'):  ('J\u2665', '\U0001F0BB'),
            ('heart', 'Q'):  ('Q\u2665', '\U0001F0BD'),
            ('heart', 'K'):  ('K\u2665', '\U0001F0BE'),

            ('diamond', 'A'):  ('A\u2666', '\U0001F0C1'),
            ('diamond', '2'):  ('2\u2666', '\U0001F0C2'),
            ('diamond', '3'):  ('3\u2666', '\U0001F0C3'),
            ('diamond', '4'):  ('4\u2666', '\U0001F0C4'),
            ('diamond', '5'):  ('5\u2666', '\U0001F0C5'),
            ('diamond', '6'):  ('6\u2666', '\U0001F0C6'),
            ('diamond', '7'):  ('7\u2666', '\U0001F0C7'),
            ('diamond', '8'):  ('8\u2666', '\U0001F0C8'),
            ('diamond', '9'):  ('9\u2666', '\U0001F0C9'),
            ('diamond', '10'): ('10\u2666', '\U0001F0CA'),
            ('diamond', 'J'):  ('J\u2666', '\U0001F0CB'),
            ('diamond', 'Q'):  ('Q\u2666', '\U0001F0CD'),
            ('diamond', 'K'):  ('K\u2666', '\U0001F0CE'),

            ('club', 'A'):  ('A\u2663', '\U0001F0D1'),
            ('club', '2'):  ('2\u2663', '\U0001F0D2'),
            ('club', '3'):  ('3\u2663', '\U0001F0D3'),
            ('club', '4'):  ('4\u2663', '\U0001F0D4'),
            ('club', '5'):  ('5\u2663', '\U0001F0D5'),
            ('club', '6'):  ('6\u2663', '\U0001F0D6'),
            ('club', '7'):  ('7\u2663', '\U0001F0D7'),
            ('club', '8'):  ('8\u2663', '\U0001F0D8'),
            ('club', '9'):  ('9\u2663', '\U0001F0D9'),
            ('club', '10'): ('10\u2663', '\U0001F0DA'),
            ('club', 'J'):  ('J\u2663', '\U0001F0DB'),
            ('club', 'Q'):  ('Q\u2663', '\U0001F0DD'),
            ('club', 'K'):  ('K\u2663', '\U0001F0DE')}

class Deck:
    """A class to create and manipulate a standard playing card 
    deck.
    
    If special args are not set, defaults to creating aa deck of 52 cards.
    
    If cards_list is specified, a Deck with exactly those cards will be created.
    
    If no_cards is specified, then a random assortment of cards (no_cards many 
    of them) will be created, with repeats or not (as specified in the argument).


    The Cards in the Deck are stored as a list; index 0 is the 'top' of the deck."""

    def __init__(self, cards_list=None, no_cards=None, repeats=False, shuffle=True, orderfirst='suit'):
        self.cards = None

        if cards_list:
            logger.debug('creating deck with specified cards')
            self.cards = cards_list
        
        elif no_cards:
            if no_cards > 0:
                logger.debug('creating deck of len {}'.format(no_cards))
                if not self.cards:
                    self.cards = []
                if repeats:
                    for i in range(no_cards):
                        self.cards.append(Card())
                else:
                    if no_cards > 52:
                        logger.warn("can't promise no repeats with a deck this big")
                    # todo - there is a better way to do this.
                    temp_set = set()
                    while len(temp_set) < no_cards:
                        c = Card()
                        if c not in temp_set:
                            temp_set.add(c)
                        else:
                            logger.debug('already found card in set')
                    self.cards = list(temp_set)
        else:
            logger.debug('creating standard 52-card desk')
            if not self.cards:
                self.cards = []
            if orderfirst == 'suit':
                for suit in _suits:
                    for rank in _ranks:
                        self.cards.append(Card(suit=suit, rank=rank))
            elif orderfirst == 'rank':
                for rank in _ranks:
                    for suit in _suits:
                        self.cards.append(Card(suit=suit, rank=rank))
            else:
                logger.error("bad order indicated: {}".format(order))
                return
            
        if shuffle:
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def get_iterator(self):
        """Return an iterator for the current Deck.
        """
        for i in range(len(self.cards)):
            yield self.cards[i]

    def deal(self, count=1):
        """Pop cards from the deck, removing them and also
        returning them as a Hand.

        Note that the Card at index 0 is the 'top' of the deck,
        and is the next one popped.

        >>> test_deck = Deck(cards=[Card('diamond', '5'), Card('spade', '6')], shuffle=False)

        >>> test_deck.deal(1)
        <Hand: len=1>
        """
        if count > len(self.cards):
            logger.error("cannot deal {} cards from a deck of size {}".format(str(count), str(len(self.cards))))
            return None
        retlist = []
        for i in range(count):
            retlist.append(self.cards.pop(0))
        return Hand(retlist)

    def __repr__(self):
        if len(self.cards) <= 0:
            return "<Deck: len {}>".format(str(len(self.cards)))
        else:
            return "<Deck: len {}; top card {}>".format(str(len(self.cards)), self.cards[0].__str__())

    def __str__(self, indent=0, width=0):
        """Print Deck.  Add newlines after printing 'indent' Cards.
        If width == 0, don't add any newlines.
        """
        return utils.str_items(self.cards, indent=indent, width=width)

    def print(self, indent=0, width=0):
        """Print Deck.  Add newlines after printing 'width' Cards.
        If width == 0, don't add any newlines.
        """
        return utils.print_items(self.cards, indent=indent, width=width)
    
    #def print_images(self, indent=0, width=0):
    #    print(utils.str_items(self.cards, fn=Card.str_image, indent=indent, width=width))

class Hand:
    """A list of Cards.
    """

    def __init__(self, cardsList=None):
        self.cards = cardsList

    def __repr__(self):
        return "<Hand: len={}>".format(len(self.cards))

    def __str__(self, indent=0, width=0):
        """Print the hand.

        >>> a = Hand([Card(suit='diamond', rank='5'), Card(suit='club', rank='10')])

        >>> a.__str__()
        '5♦  10♣ '
        """
        return utils.str_items(self.cards, indent=indent, width=width)
        
    def print(self, indent=0, width=0):
        """Print the card in a simple way (<rank><suit>).
        Same as __str__().

        >>> a = Hand([Card(suit='diamond', rank='5'), Card(suit='club', rank='10')])

        >>> a.print()
        '5♦  10♣ '
        """
        return utils.print_items(self.cards, indent=indent, width=width)

    #def print_images(self, indent=0, width=0):
    #    print(utils.str_items(self.cards, fn=Card.str_image, indent=indent, width=width))

class Card:
    """A playing card.  Has a rank and suit.
    """

    def __init__(self, suit=None, rank=None):
        """Create a Card with specified suit and rank.

        If either is not specified, a random suit/rank
        will be assigned.
        """
        import random

        if not suit:
            self.suit = random.choice(_suits)
        else:
            if suit not in _suits:
                logger.error('suit "{}" not one of {}'.format(suit, str(_suits)))
            else:
                self.suit = suit

        if not rank:
            self.rank = random.choice(_ranks)
        else:
            if rank not in _ranks:
                logger.error('rank "{}" not one of {}'.format(rank, str(_ranks)))
            else:
                self.rank = rank

    def __eq__(self, other):
        return (self.suit == other.suit and self.rank == other.rank)

    def __hash__(self):
        return hash((self.suit, self.rank))

    def get_rank(self):
        """Return the rank of the card.

        >>> a = Card(suit='diamond', rank='5')

        >>> a.get_rank()
        '5'
        """
        return self.rank

    def get_suit(self):
        """Return the suit of the card.

        >>> a = Card(suit='diamond', rank='5')

        >>> a.get_suit()
        'diamond'
        """
        return self.suit

    def get_value(self):                                                                                                                                                                                                                                                       
        """All of these values won't make sense                                                                                                                                                                                                                               
        for every game.                                                                                                                                                                                                                                                       

        >>> a = Card(suit='diamond', rank='5')

        >>> a.get_value()
        5
        """
        return _rankVals[self.rank]

    def __repr__(self):
        return "<Card: suit={}, rank={}>".format(str(self.suit), str(self.rank))

    def __str__(self):
        """Print the card in a simple way (<rank><suit>).

        >>> a = Card(suit='diamond', rank='5')

        >>> a.__str__()
        '5♦'
        """
        return _ppCodes[(self.suit, self.rank)][0]

    def str_image(self):
        return __ppCodes[(self.suit, self.rank)][1]

    def print(self):
        """Print the card in a simple way (<rank><suit>).
        Same as __str__().

        >>> a = Card(suit='diamond', rank='5')

        >>> a.print()
        '5♦'
        """
        print('{0:4}'.format(self.__str__()), end='')

    def print_image(self):
        """Print the unicode image of the card.

        >>> a = Card(suit='diamond', rank='5')

        >>> a.print_image()
        '🃅'
        """
        print('{0:2}'.format(_ppCodes[(self.suit, self.rank)][1]), end='')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
