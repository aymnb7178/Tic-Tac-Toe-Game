"""Tic-Tac-Toe with an unbeatable minimax (alpha-beta) computer player.

Board: a list of 9 cells, each "X", "O" or " " (index 0 = top-left, 8 = bottom-right).
Run:  python tictactoe.py
"""
from __future__ import annotations

from typing import List, Optional, Tuple

EMPTY = " "
LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def new_board() -> List[str]:
    return [EMPTY] * 9


def winner(board: List[str]) -> Optional[str]:
    for a, b, c in LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board: List[str]) -> bool:
    return EMPTY not in board


def moves(board: List[str]) -> List[int]:
    return [i for i, v in enumerate(board) if v == EMPTY]


def other(player: str) -> str:
    return "O" if player == "X" else "X"


def _minimax(board: List[str], player: str, me: str, alpha: int, beta: int, depth: int) -> int:
    w = winner(board)
    if w == me:
        return 10 - depth          # win sooner is better
    if w is not None:
        return depth - 10          # lose later is better
    if is_full(board):
        return 0
    maximizing = player == me
    best = -100 if maximizing else 100
    for m in moves(board):
        board[m] = player
        score = _minimax(board, other(player), me, alpha, beta, depth + 1)
        board[m] = EMPTY
        if maximizing:
            best = max(best, score)
            alpha = max(alpha, best)
        else:
            best = min(best, score)
            beta = min(beta, best)
        if beta <= alpha:
            break
    return best


def best_move(board: List[str], player: str) -> int:
    """Return the best cell index for ``player``. Raises ValueError if the game is over."""
    if winner(board) or is_full(board):
        raise ValueError("game is already over")
    best_score, best = -101, -1
    for m in moves(board):
        board[m] = player
        score = _minimax(board, other(player), player, -100, 100, 1)
        board[m] = EMPTY
        if score > best_score:
            best_score, best = score, m
    return best


def render(board: List[str]) -> str:
    rows = [" | ".join(board[r * 3:r * 3 + 3]) for r in range(3)]
    return "\n---------\n".join(rows)


def ask_move(board: List[str]) -> int:
    while True:
        raw = input("Your move (1-9, top-left=1): ").strip()
        if raw.isdigit() and 1 <= int(raw) <= 9 and board[int(raw) - 1] == EMPTY:
            return int(raw) - 1
        print("Invalid or taken cell.")


def play() -> Tuple[str, List[str]]:
    board, human, computer = new_board(), "X", "O"
    turn = "X"
    print("You are X, the computer is O.\n")
    while not winner(board) and not is_full(board):
        print(render(board) + "\n")
        if turn == human:
            board[ask_move(board)] = human
        else:
            board[best_move(board, computer)] = computer
        turn = other(turn)
    print(render(board) + "\n")
    w = winner(board)
    print(f"{w} wins!" if w else "Draw.")
    return (w or "draw"), board


if __name__ == "__main__":
    play()
