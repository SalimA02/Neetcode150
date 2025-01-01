class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = collections.defaultdict(set)
        row = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row[r]) or (board[r][c] in column[c]) or (board[r][c] in squares[r//3, c//3]):
                    return False
                column[c].add(board[r][c])
                row[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])    
        print(column, row, squares)
        return True
