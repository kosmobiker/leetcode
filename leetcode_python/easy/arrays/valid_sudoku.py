"""
Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

from typing import List
from collections import Counter


class Solution:
    def is_okay(self, seq: List[str]) -> bool:
        """Checks if list contains correct values

        Args:
            seq (List[str]): input sequence of elements

        Returns:
            bool: True is okay otherwise False
        """
        d = {k: v for (k, v) in Counter(seq).items() if v > 1}
        if len(d) > 1:
            return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Check rows"""
        for row in board:
            if not self.is_okay(row):
                return False
        """Check columns"""
        for i in range(0, len(board)):
            column = [item[i] for item in board]
            if not self.is_okay(column):
                return False
        """Check 3x3 boxes"""
        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                box = (
                    board[row][column : column + 3]
                    + board[row + 1][column : column + 3]
                    + board[row + 2][column : column + 3]
                )
                if not self.is_okay(box):
                    return False
        return True


if __name__ == "__main__":
    s = Solution()

    # Test case 1
    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    expected_output1 = True
    r1 = s.isValidSudoku(board1)
    assert (
        r1 == expected_output1
    ), f"Test Case 1 Failed: expected output {expected_output1}, but got {r1}"

    # Test case 2
    board2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    expected_output2 = False
    r2 = s.isValidSudoku(board2)
    assert (
        r2 == expected_output2
    ), f"Test Case 2 Failed: expected output {expected_output2}, but got {r2}"
