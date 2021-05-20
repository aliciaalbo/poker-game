import random

class Deck():
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))
                # print(f"{value} of {suit}")

    def showDeck(self):
        # self.cards contains instances of Card class so can use prev show method
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            # choose number to left, iterating backwards
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]
    def drawCard(self):
        #pop card off "top" of deck
        return self.cards.pop()


class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def show(self):
        print(f"{self.value} of {self.suit}")

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self 
    
    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()
