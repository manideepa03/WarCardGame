# WarCardGame

War Game Rules: https://en.wikipedia.org/wiki/War_(card_game).

## Assumptions

```
1. Input:
    -  4 suits : Hearts, Clubs, Spades and Diamonds.
    - 13 ranks : 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'
    - 1 deck of 52 cards
    - 2 players

2. Output:
    - 1 winner: player that has all the cards
    - Console output

3. Corner cases:
    - Play the game until one of the player runs of cards in the hand
    - Empty the table and war cards list after every round
    - When both the players place the same rank card, war is started

```

## Technologies

Install the following
**Core**

- Python
- Pip
- Pytest

**Testing**

- Pytest

## Usage

All the code is in the WarGame.py file and tests in tests.py file

Clone the repo, play a war game by entering the player names

- Run the game

```
$ python WarGame.py
```

- Run the tests

```
$ pytest tests.py
```

- Run the coverage

```
$ coverage run WarGame.py
$ coverage report
```

- Coverage report

```
Name         Stmts   Miss  Cover
--------------------------------
WarGame.py     101      5    95%
--------------------------------
TOTAL          101      5    95%

```

## Further improvements with more time

- Build a GUI to play the game
- Setup game with more than 2 players
- Refactor code with each class in separate files
