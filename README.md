# Tic-Tac-Toe Game

Console Tic-Tac-Toe in Python against a computer player that uses **minimax with alpha-beta pruning**, so it never loses.

> Written with AI assistance (Claude), reviewed and published by the repository owner.

## Run

```bash
python tictactoe.py          # you are X, the computer is O; enter 1-9 (top-left = 1)
python -m unittest -v        # 8 tests
```

Python 3.8+ and no extra packages.

## How it works

`best_move()` tries every legal move, scores the resulting game tree with minimax (win = `10 - depth`, loss = `depth - 10`, draw = 0 so it wins fast and loses slowly) and skips branches that cannot change the result (alpha-beta pruning). The board is a plain list of 9 cells.

## Verified

- ✅ 8 unit tests, including an **exhaustive** check: the computer plays against *every possible* sequence of opponent moves, once as X and once as O, and never loses.
- ✅ Takes an immediate win, blocks an immediate loss, does not mutate the board it is given.
- 🟡 The interactive prompt was exercised with scripted input only.

## Possible next steps

Two-player mode, difficulty levels (random / perfect), a simple GUI.

## Author

Aymen - [github.com/aymnb7178](https://github.com/aymnb7178)
