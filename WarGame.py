import random

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 1]
suits = ['Heart', 'Diamond', 'Spade', 'Club']


class Card:

    def __init__(self):
        self.suits = suits
        self.ranks = ranks

    def deck(self):
        self.deckCards = [(suit, rank)
                          for suit in self.suits for rank in self.ranks]
        return self.deckCards

    def shuffle(self):
        random.shuffle(self.deckCards)


class Player:
    def __init__(self, playerName1, playerName2):
        self.playerName1 = playerName1
        self.playerName2 = playerName2
        self.card = Card()
        self.card.deck()
        self.card.shuffle()

    def split_cards(self):
        return (self.card.deckCards[:26], self.card.deckCards[26:])


def main():
    print("Welcome to the War Card Game")
    player1 = input("Enter Player 1 Name :")
    player2 = input("Enter Player 2 Name :")
    play = Player(player1, player2)
    p1cards, p2cards = play.split_cards()

    print(player1, "'s cards =============")
    print(p1cards)

    print(player2, "'s cards =============")
    print(p2cards)


if __name__ == '__main__':
    main()
