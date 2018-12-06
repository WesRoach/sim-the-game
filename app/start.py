import sys

import random


# stacks consist of cards ascending/descending
class Stack:
    def __init__(self, order):
        self.order = order
        self.cards = [1 if order == "asc" else 100]

    def getOrder(self):
        return self.order

    def getCards(self):
        return self.cards

    def getTopCard(self):
        return self.cards[-1]

    def placeCard(self, card):
        if self.getOrder() == "asc":
            if card > self.getTopCard():
                self.cards.append(card)
                return True
            else:
                return False
        else:
            if card < self.getTopCard():
                self.cards.append(card)
                return True
            else:
                return False


# board is made of four stacks
class Board:
    def __init__(self):
        self.stacks = [Stack("asc") for i in range(0, 2)]
        self.stacks.extend([Stack("desc") for i in range(0, 2)])

    def getStacks(self):
        return self.stacks

    def getTopCards(self):
        return [
                    {
                        'card': stack.getTopCard(),
                        'order': stack.getOrder()
                    }
                    for stack in self.getStacks()
                ]


# deck is shuffled cards 2 through 99
class Deck:
    def __init__(self):
        self.deck = [i for i in range(2, 100)]
        random.shuffle(self.deck)
        # start index at 0
        self.topCard = 0

    # What cards are available in Deck
    def getRemainingCards(self):
        return self.deck[self.topCard :]

    def getOriginalCards(self):
        return self.deck

    def getRemainingCardsCount(self):
        return 100 - self.topCard

    # Remove N cards from deck and return it
    def drawCards(self, n: int):
        draw_cards = self.deck[self.topCard : (self.topCard + int(n))]
        self.topCard += int(n)
        return draw_cards


# player's hand contains cards
class Player:
    def __init__(self):
        self.hand = []

    def swap_by_value(self, outCard, inCard):
        """
        Replaces card in Player's hand.
        """
        self.hand[self.hand.index(outCard)] = inCard


# Game logic
class Game:
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

    def input_card_stack(self):
        while True:
            try:
                selected_card, selected_stack = map(int, input(": ").split())

                if selected_stack > 4 or selected_stack < 1:
                    print("[Stack] must be between 1 and 4.")
                    continue
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                print("Please enter a [Card] Index, [Space], [Stack] Index")
                print("Example places card 3 on stack 1:")
                print("3 1")
                continue
            else:
                break
        return selected_card, selected_stack

    def display_hand(self, idx, player):
        print(f"-- Player {idx}'s Hand --")
        for idx, player_card in enumerate(player.hand):

            top_cards = self.board.getTopCards()
            diff = [player_card - top_card['card'] for top_card in top_cards]

            print(f"[{idx + 1}] {player_card}   Diff: {diff}")

    def play(self):
        while self.deck.getRemainingCardsCount() > 0:
            # Print Game state
            print("\n=== The Game ===")
            print("Cards in Deck: %s" % len(self.deck.getRemainingCards()))
            print("-- Board --")
            for idx, stack in enumerate(self.board.getStacks()):
                _topCard = stack.getTopCard()
                _order = stack.getOrder()
                print(f"[{idx + 1}] {_order} Top Card: {_topCard}")

            for idx, player in enumerate(self.players):
                self.display_hand(idx, player)

            # Player Options
            print("")
            print("[Card] [Stack]")
            selected_card, selected_stack = self.input_card_stack()

            # convert card_idx to card
            card = self.players[0].hand[selected_card - 1]

            # try to place card on stack
            if self.board.stacks[selected_stack - 1].placeCard(card):
                # if card placed - remove from player's hand
                # self.players[0].hand.remove(card)
                # cards_to_draw_num = self.cards_per_player - len(self.players[0].hand)
                # self.players[0].hand.extend(self.deck.drawCards(cards_to_draw_num))
                self.players[0].swap_by_value(card, self.deck.drawCards(1).pop())


if __name__ == "__main__":
    # num_players = input("Player Count: ")
    # cards_per_player = input("Cards per Player: ")
    num_players = 1
    cards_per_player = 7

    # start a game
    game = Game(num_players, cards_per_player)
    game.play()
