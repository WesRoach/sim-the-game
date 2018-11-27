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

    def placeCard(self, card):
        if self.getOrder() == 'asc':
            if card > self.getTopCard():
                self.cards.append(card)
            else:
                return -1
        else:
            if card < self.getTopCard():
                self.cards.append(card)
            else:
                return -1


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
    def drawCards(self, n: int):
        draw_cards = self.deck[self.topCard:(self.topCard + int(n))]
        self.topCard += int(n)
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
        while self.deck.getRemainingCardsCount() > 0:
            # Print Game state
            print("\n=== The Game ===")
            print('Cards in Deck: %s' % len(self.deck.getRemainingCards()) )
            print('-- Board --')
            for idx, stack in enumerate(self.board.getStacks()):
                _topCard = stack.getTopCard()
                _order = stack.getOrder()
                print(f'[{idx + 1}] {_order} Top Card: {_topCard}')

            for idx, player in enumerate(self.players):
                print(f'-- Player {idx}\'s Hand --')
                # print(player.hand)
                for idx, card in enumerate(player.hand):
                    print(f'[{idx + 1}] {card}')

            # Player Options
            print("")
            print("[D]raw Cards, or [P]lay")
            draw_or_play = input(": ")

            if draw_or_play in ('D', 'd'):
                cards_to_draw_num = \
                    self.cards_per_player - len(self.players[0].hand)
                # TODO(Wes): player index update
                self.players[0].hand.extend(self.deck.drawCards(cards_to_draw_num))
            elif draw_or_play in ('P', 'p'):
                card = int(input("Card: "))
                stack = int(input("Stack: "))
                # try to place card on stack
                self.board.stacks[stack - 1].placeCard(card)
                # TODO(Wes): this index is garbage
                self.players[0].hand.remove(card)
            else:
                pass
                # TODO(Wes)


if __name__ == "__main__":
    num_players = input("Player Count: ")
    cards_per_player = input("Cards per Player: ")

    # start a game
    game = Game(num_players, cards_per_player)
    game.play()
