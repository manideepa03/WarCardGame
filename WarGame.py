import random


class Card:
    """Represents all the cards in the game"""

    def __init__(self):
        self.suits = ['Heart', 'Diamond', 'Spade', 'Club']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.deckCards = []

    def deck(self):
        """Creates a new deck of 52 cards

        Returns:
            deckCards: list of all the cards
        """
        self.deckCards = [(suit, rank)
                          for suit in self.suits for rank in self.ranks]

        return self.deckCards

    def shuffle(self):
        """Random shuffling of deck cards"""
        random.shuffle(self.deckCards)

    def split_cards(self):
        """Splits the 52 deck of cards into 2 halfs

        Returns:
            list: Two lists with 26 cards in each
        """
        return (self.deckCards[:26], self.deckCards[26:])


class Player:

    """Represents a player with name and cards the player has"""

    def __init__(self, player):
        self.player = player
        self.hand = None
        if not isinstance(player, str):
            raise TypeError("please enter a string")

    def show_card(self):
        """Returns top card on the player's deck """
        return self.hand.pop(0)

    def take_card(self, taken):
        """adds the cards at bottom of player's deck """
        self.hand.extend(taken)


class Table:
    """Represents the cards present on the table"""

    def __init__(self):
        self.tableCards = []
        self.warCards = []

    def war_cards(self, warhand):
        """ Takes the cards in player hand and returns top three cards 

        Args:
            warhand (list): List of cards in player hand

        Returns:
            list: top three cards from the players hand
        """
        self.warCards = []
        if len(warhand) < 3:
            return warhand
        else:
            for i in range(3):
                self.warCards.append(warhand.pop(0))

            return self.warCards


class Game:

    """ Represents all the actions in the game"""

    def __init__(self, player1, player2):
        self.p1cards = None
        self.p2cards = None
        self.p1 = Player(player1)
        self.p2 = Player(player2)
        self.table = Table()
        self.card = Card()

    def give_cards(self):
        """ Gives the cards equally to two players"""
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
        """ Gets the top 3 cards from the each player and adds it to the deck of cards on the table"""

        self.table.tableCards.extend(self.table.war_cards(self.p1.hand))
        self.table.tableCards.extend(self.table.war_cards(self.p2.hand))

    def winner(self):
        """Determines which player is the winner of the game
        """
        if len(self.p1.hand) != 0:
            print(self.p1.player, 'Wins the Game')
            return self.p1.player + 'wins the game '

        else:
            print(self.p2.player, 'Wins the Game')
            return self.p2.player + 'wins the game '

    def play_game(self):
        """ Plays the game until one of the player has no cards"""

        self.round_count = 0

        while len(self.p1.hand) != 0 and len(self.p2.hand) != 0:
            self.round_count += 1
            print("\n")
            print("New round number", self.round_count)
            print("Here are the current standings")
            print(self.p1.player + " has the count:", len(self.p1.hand))
            print(self.p2.player + " has the count:", len(self.p2.hand))
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
                print("===============War has started====================")
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

        self.winner()


def main():
    """Runs the main loop of the game
    """
    print("Welcome to the War Card Game")

    player1 = input("Enter Player 1 Name :")
    player2 = input("Enter Player 2 Name :")

    game = Game(player1, player2)
    game.give_cards()
    game.play_game()


if __name__ == '__main__':
    main()
