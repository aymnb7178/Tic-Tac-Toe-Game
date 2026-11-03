import unittest

from tictactoe import best_move, is_full, moves, new_board, other, winner


class TestRules(unittest.TestCase):
    def test_winner_all_lines(self):
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            bd = new_board()
            bd[a] = bd[b] = bd[c] = "X"
            self.assertEqual(winner(bd), "X")

    def test_no_winner_and_full(self):
        self.assertIsNone(winner(new_board()))
        self.assertTrue(is_full(list("XOXOXOOXO")))


class TestAI(unittest.TestCase):
    def test_takes_winning_move(self):
        bd = list("XX OO    ")
        self.assertEqual(best_move(bd, "X"), 2)

    def test_blocks_opponent(self):
        bd = list("XX  O    ")
        self.assertEqual(best_move(bd, "O"), 2)

    def test_game_over_raises(self):
        with self.assertRaises(ValueError):
            best_move(list("XXXOO    "), "O")

    def test_best_move_does_not_mutate_board(self):
        bd = list("X   O    ")
        before = bd[:]
        best_move(bd, "X")
        self.assertEqual(bd, before)

    def test_computer_never_loses_as_O(self):
        results = []
        self._explore(new_board(), "X", "O", results)
        self.assertGreater(len(results), 100)
        self.assertNotIn("X", results)

    def test_computer_never_loses_as_X(self):
        results = []
        self._explore(new_board(), "X", "X", results)
        self.assertNotIn("O", results)

    def _explore(self, board, turn, computer, results):
        w = winner(board)
        if w or is_full(board):
            results.append(w or "draw")
            return
        if turn == computer:
            m = best_move(board, computer)
            board[m] = computer
            self._explore(board, other(turn), computer, results)
            board[m] = " "
        else:
            for m in moves(board):
                board[m] = turn
                self._explore(board, other(turn), computer, results)
                board[m] = " "


if __name__ == "__main__":
    unittest.main()
