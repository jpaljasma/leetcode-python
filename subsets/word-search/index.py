from typing import List

"""
Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.

The same letter cell may not be used more than once.
"""


class Solution:

    """
    Recursive function will take in board, word, position of current char, and current string we have found in our search
    """

    def _solution(self, board: List[List[str]], word: str, x: int, y: int, cur: str):
        # check if current position is out of bounds,
        # or if we have visited the board
        # (we mark it empty as we cannot use cell twice)

        if x < 0 or x >= len(board) or y < 0 or y >= len(board[x]) or board[x][y] == "":
            return False

        # add character to the current string
        cur += board[x][y]

        # if length of the current word is bigger than word we search, return False
        if len(cur) > len(word):
            return False

        # if a last element of the current string is a different character than from same position in our target word, return False
        last_pos = len(cur) - 1
        if cur[last_pos] != word[last_pos]:
            return False

        # if string is equal, return True
        if cur == word:
            return True

        temp = board[x][y]
        # indicate we visited this
        board[x][y] = ""

        # start the loop of 4 over neighbors with deltas
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        for i in range(0, 4):
            if self._solution(board, word, x + dx[i], y + dy[i], cur):
                return True

        board[x][y] = temp

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and self._solution(board, word, i, j, ""):
                    return True

        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"

    s = Solution()
    print(s.exist(board, word))
