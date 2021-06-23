import pytest
import unittest
from WarGame import Card
from WarGame import Player
from WarGame import Game
from WarGame import Table


@pytest.fixture
def card():

    return Card()


@pytest.fixture
def game():

    return Game("Abby", "John")


def test_card_init(card):

    assert card.suits == ['Heart', 'Diamond', 'Spade', 'Club']
    assert card.ranks == [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    assert card.deckCards == []


def test_deck(card):

    card.deckCards = card.deck()
    assert len(card.deckCards) == 52


def test_split_cards(card):

    card.deckCards = card.deck()
    p1, p2 = card.split_cards()
    assert len(p1) == 26
    assert len(p2) == 26


def test_player_init():

    p1 = Player("Abby")
    p2 = Player("John")
    assert "Abby" == p1.player
    assert "John" == p2.player


def test_show_card():
    p1 = Player("Abby")
    p2 = Player("John")
    with pytest.raises(TypeError):
        Player(9)

    p1.hand = [('Spade', 10), ('Club', 10)]
    p2.hand = [('Diamond', 3), ('Spade', 2)]
    assert p1.show_card() == ('Spade', 10)
    assert p2.show_card() == ('Diamond', 3)


def test_give_cards(game):
    p1 = Player("Abby")
    p2 = Player("John")
    assert p1.hand == None

    game.give_cards()

    assert len(game.p1.hand) == 26
    assert len(game.p2.hand) == 26


def test_winner(game):
    p1 = Player("Abby")
    p2 = Player("John")

    game.p1.hand = [('Diamond', 7), ('Diamond', 8), ('Heart', 3), ('Heart', 5), ('Spade', 'J'), ('Club', 2), ('Diamond', 3), ('Club', 9), ('Spade', 'K'), ('Spade', 7), ('Heart', 2), ('Spade', 4), ('Diamond', 6), ('Heart', 6), ('Heart', 7), ('Heart', 'Q'), ('Heart', 4), ('Diamond', 5), ('Spade', 6), ('Diamond', 'Q'), ('Heart', 10), ('Club', 3), ('Spade', 10), ('Heart', 'J'), ('Diamond', 10), ('Club', 10),
                    ('Spade', 3), ('Heart', 9), ('Club', 8), ('Club', 5), ('Spade', 8), ('Club', 6), ('Spade', 2), ('Heart', 8), ('Heart', 'K'), ('Spade', 5), ('Diamond', 'J'), ('Club', 4), ('Diamond', 4), ('Club', 'Q'), ('Club', 'J'), ('Diamond', 9), ('Spade', 9), ('Club', 7), ('Diamond', 'K'), ('Club', 'K'), ('Diamond', 2), ('Spade', 'A'), ('Diamond', 'A'), ('Club', 'A'), ('Heart', 'A'), ('Spade', 'Q')]
    game.p2.hand = []

    assert game.winner() == game.p1.player + 'wins the game '

    game.p2.hand = [('Diamond', 7), ('Diamond', 8), ('Heart', 3), ('Heart', 5), ('Spade', 'J'), ('Club', 2), ('Diamond', 3), ('Club', 9), ('Spade', 'K'), ('Spade', 7), ('Heart', 2), ('Spade', 4), ('Diamond', 6), ('Heart', 6), ('Heart', 7), ('Heart', 'Q'), ('Heart', 4), ('Diamond', 5), ('Spade', 6), ('Diamond', 'Q'), ('Heart', 10), ('Club', 3), ('Spade', 10), ('Heart', 'J'), ('Diamond', 10), ('Club', 10),
                    ('Spade', 3), ('Heart', 9), ('Club', 8), ('Club', 5), ('Spade', 8), ('Club', 6), ('Spade', 2), ('Heart', 8), ('Heart', 'K'), ('Spade', 5), ('Diamond', 'J'), ('Club', 4), ('Diamond', 4), ('Club', 'Q'), ('Club', 'J'), ('Diamond', 9), ('Spade', 9), ('Club', 7), ('Diamond', 'K'), ('Club', 'K'), ('Diamond', 2), ('Spade', 'A'), ('Diamond', 'A'), ('Club', 'A'), ('Heart', 'A'), ('Spade', 'Q')]
    game.p1.hand = []

    assert game.winner() == game.p2.player + 'wins the game '
