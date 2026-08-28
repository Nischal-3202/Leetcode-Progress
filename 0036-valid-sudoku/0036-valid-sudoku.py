class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                box=(r//3)*3+(c//3)
                if board[r][c]==".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[box]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[box].add(board[r][c])
        return True