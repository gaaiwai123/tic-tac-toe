import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        bord = [
            ['O', 'O', 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(bord), 'O')

    # TODO: Test all functions from logic.py!
    def test_make_empty_board(self):
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.make_empty_board(), board)
    def test_other_player(self):
        self.assertEqual(logic.other_player('X'), 'O')
        self.assertEqual(logic.other_player('O'), 'X')
    def test_print_board(self):
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        result=\
"""1 | 2 | 3 
---------
4 | 5 | 6 
---------
7 | 8 | 9 
"""
        self.assertEqual(logic.print_board(board), result)
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['X', 'O', 'X'],
        ]
        result=\
"""X | O | X 
---------
O | X | O 
---------
X | O | X 
"""
        self.assertEqual(logic.print_board(board), result)
    def test_make_move(self):
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        board1 = [
            ['X', None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.make_move(board, 'X', 1), (True,board1))
        board2 = [
            ['X', None, None],
            ['O', None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.make_move(board1, 'O', 4), (True,board2))
        board3 = [
            ['X', None, None],
            ['O', None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.make_move(board2, 'X', 4), (False,board3))
        board4 = [
            ['X', None, None],
            ['O', None, None],
            [None, None, 'X'],
        ]
        self.assertEqual(logic.make_move(board3, 'X', 9), (True,board4))
    def test_check_full(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['X', 'O', 'X'],
        ]
        self.assertEqual(logic.check_full(board), True)
        board1 = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['X', 'O', None],
        ]
        self.assertEqual(logic.check_full(board1), False)

if __name__ == '__main__':
    unittest.main()
