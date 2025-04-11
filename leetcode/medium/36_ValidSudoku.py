class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                val = board[i][j]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)
        
        for j in range(len(board)):
            seen = set()
            for i in range(len(board)):
                val = board[i][j]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)

        for box_i in range(0, len(board), 3):
            for box_j in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_i + i][box_j + j]
                        if val != ".":
                            if val in seen:
                                return False
                            seen.add(val)

        return True