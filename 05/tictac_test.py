import unittest
from unittest.mock import patch
from tictac import TicTacGame, step_processing, validate_input


class TestTicTacGame(unittest.TestCase):
    def setUp(self):
        self.tictac = TicTacGame()

    @patch("builtins.input", side_effect=["X"])
    def test_validate_input_1(self, mock_inputs):
        result = validate_input()
        self.assertEqual(result, ("X", "O"))

    @patch("builtins.input", side_effect=["O"])
    def test_validate_input_2(self, mock_inputs):
        result = validate_input()
        self.assertEqual(result, ("O", "X"))

    @patch("builtins.input", side_effect=["8"])
    def test_step_processing(self, mock_inputs):
        result = step_processing([1, 3, 5, 8, 9])
        self.assertEqual(result, 8)

    def test_check_rows(self):
        self.tictac.board = ["X", 2, 3, "O", "O", "O", "X", "X", 9]
        self.assertTrue(self.tictac.check_rows())
        self.tictac.board = ["X", 2, "O", "O", "O", 6, "X", "X", "X"]
        self.assertTrue(self.tictac.check_rows())

    def test_check_columns(self):
        self.tictac.board = ["X", 2, 3, "X", "O", "O", "X", 8, 9]
        self.assertTrue(self.tictac.check_columns())
        self.tictac.board = [1, 2, "O", "X", 5, "O", "X", "X", "O"]
        self.assertTrue(self.tictac.check_columns())

    def test_check_diagonals(self):
        self.tictac.board = ["X", 2, 3, "O", "X", "O", 7, 8, "X"]
        self.assertTrue(self.tictac.check_diagonals())
        self.tictac.board = [1, 2, "O", "X", "O", "X", "O", "X", 9]
        self.assertTrue(self.tictac.check_diagonals())

    def test_check_winner(self):
        self.tictac.board = ["X", 2, "X", "O", "X", "O", 7, 8, "O"]
        self.assertFalse(self.tictac.check_winner())
        self.tictac.board = [1, "O", 3, "X", "O", "X", "X", "O", 9]
        self.assertTrue(self.tictac.check_winner())


if __name__ == "__main__":
    unittest.main()
