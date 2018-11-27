import random


# stacks consist of cards ascending/descending
class Stack():
    def __init__(self, order):
        self.order = order
        self.cards = [1 if order == 'asc' else 100]

    def getOrder(self):
        return self.order

    def getCards(self):
        return self.cards

    def getTopCard(self):
        return self.cards[-1]


# board is made of four stacks
class Board():
    def __init__(self):
        self.stacks = [Stack('asc') for i in range(0, 2)]
        self.stacks.extend([Stack('desc') for i in range(0, 2)])

    def getStacks(self):
        return self.stacks


# deck is shuffled cards 2 through 99
class Deck():
    def __init__(self):
        self.deck = [i for i in range(2, 100)]
        random.shuffle(self.deck)
        # start index at 0
        self.topCard = 0

    # What cards are available in Deck
    def getRemainingCards(self):
        return self.deck[self.topCard:]

    def getOriginalCards(self):
        return self.deck

    def getRemainingCardsCount(self):
        return 100 - self.topCard

    # Remove N cards from deck and return it
    def drawCards(self, n):
        draw_cards = self.deck[self.topCard:n]
        self.topCard += n
        return draw_cards


# player's hand contains cards
class Player():
    def __init__(self):
        self.hand = []


# Game logic
class Game():
    def __init__(self, num_players, cards_per_player):
        self.players = [Player() for _ in range(0, int(num_players))]
        # lay down the board and shuffle the deck
        self.board = Board()
        self.deck = Deck()

        # set rules
        self.num_players = num_players
        self.cards_per_player = cards_per_player

        # give each player cards_per_player
        for player in self.players:
            player.hand = self.deck.drawCards(self.cards_per_player)

    def play(self):
        pass


if __name__ == "__main__":
    num_players = input("Player Count: ")
    cards_per_player = input("Cards per Player: ")

    # start a game
    game = Game(num_players, cards_per_player)
    game.play()
