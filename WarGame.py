import random


class Card:

    def __init__(self):
        self.suits = ['Heart', 'Diamond', 'Spade', 'Club']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.deckCards = []

    def deck(self):
        self.deckCards = [(suit, rank)
                          for suit in self.suits for rank in self.ranks]
        return self.deckCards

    def shuffle(self):
        random.shuffle(self.deckCards)

    def split_cards(self):
        return (self.deckCards[:26], self.deckCards[26:])


class Player:
    def __init__(self, player):
        self.player = player
        self.hand = None

    def show_card(self):
        return self.hand.pop(0)

    def take_card(self, taken):
        self.hand.extend(taken)


class Table:
    def __init__(self):
        self.tableCards = []
        self.warCards = []

    def war_cards(self, hand):
        if len(hand) < 3:
            return hand
        else:
            for i in range(3):
                self.warCards.append(hand.pop(0))
            return self.warCards


class Game:
    def __init__(self, player1, player2):
        self.p1cards = None
        self.p2cards = None
        self.p1 = Player(player1)
        self.p2 = Player(player2)
        self.table = Table()
        self.card = Card()

    def give_cards(self):
        self.card.deck()
        self.card.shuffle()

        self.p1.hand, self.p2.hand = self.card.split_cards()

        print(self.p1.player, "'s cards =============\n")
        print(self.p1.hand)
        print("\n")

        print(self.p2.player, "'s cards =============\n")
        print(self.p2.hand)
        print("\n")

    def war_mode(self):
        p1warcards = None
        p2warcards = None
        p1warcards = self.table.war_cards(self.p1.hand)
        p2warcards = self.table.war_cards(self.p2.hand)

        self.table.tableCards.extend(p1warcards)
        self.table.tableCards.extend(p2warcards)
        return self.table.tableCards

    def winner(self):
        if len(self.p1.hand) != 0:
            print(self.p1.player, 'Wins the Game')

        else:
            print(self.p2.player, 'Wins the Game')

    def play_game(self):

        self.round_count = 0

        while len(self.p1.hand) != 0 and len(self.p2.hand) != 0:
            self.round_count += 1

            print("New round")
            print("Here are the current standings")
            print(self.p1.player + " has the count:"+str(len(self.p1.hand)))
            print(self.p2.player + " has the count:"+str(len(self.p2.hand)))
            print("Play a card!")
            print("\n")

            self.table.tableCards = []
            self.p1card = None
            self.p2card = None

            self.p1card = self.p1.show_card()
            self.p2card = self.p2.show_card()

            print(self.p1.player, "has ", self.p1card)
            print(self.p2.player, "has ", self.p2card)

            self.table.tableCards.append(self.p1card)
            self.table.tableCards.append(self.p2card)

            if self.p1card[1] == self.p2card[1]:
                print("War has started")
                self.war_mode()

                if self.card.ranks.index(self.p1card[1]) < self.card.ranks.index(self.p2card[1]):
                    self.p1.take_card(self.table.tableCards)
                else:
                    self.p2.take_card(self.table.tableCards)
                self.table.warCards = []

            else:
                if self.card.ranks.index(self.p1card[1]) < self.card.ranks.index(self.p2card[1]):
                    self.p1.take_card(self.table.tableCards)
                else:
                    self.p2.take_card(self.table.tableCards)
            # if self.round_count == 2:
            #     exit()
        self.winner()


def main():
    print("Welcome to the War Card Game")

    player1 = input("Enter Player 1 Name :")
    player2 = input("Enter Player 2 Name :")

    game = Game(player1, player2)
    game.give_cards()
    game.play_game()


if __name__ == '__main__':
    main()
