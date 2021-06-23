import pytest
import unittest
from WarGame import Card
from WarGame import Player
from WarGame import Game
from WarGame import Table


def card():
    return Card()


def test_card_init():
    card = Card()

    assert card.suits == ['Heart', 'Diamond', 'Spade', 'Club']
    assert card.ranks == [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    assert card.deckCards == []


def test_deck():

    card = Card()
    card.deckCards = card.deck()
    assert len(card.deckCards) == 52


def test_split_cards():
    card = Card()
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
    p1.hand = [('Spade', 10), ('Club', 10)]
    p2.hand = [('Diamond', 3), ('Spade', 2)]
    assert p1.show_card() == ('Spade', 10)
    assert p2.show_card() == ('Diamond', 3)
    assert p2.show_card() == ('Diamond', 10)
