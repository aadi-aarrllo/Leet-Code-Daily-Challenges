'''The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9'''

# Solution ----------------------------------------------------------------------------------------------------------------------------------

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def create_board(state):
            board = []
            for row in state:
                board.append(''.join(row))
            return board
        
        def is_valid(board, row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i][j] == 'Q':
                    return False
            
            return True
        
        def solve(board, row):
            if row == n:
                result.append(create_board(board))
                return
            
            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = 'Q'
                    solve(board, row + 1)
                    board[row][col] = '.'
        
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        solve(board, 0)
        return result
