class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW=len(board)
        COL=len(board[0])
        
        def helper(row,col,l):
            if l==len(word):
                return True
            if row < 0 or row >= ROW or col < 0 or col >= COL or board[row][col] != word[l]:
                return False
            
            temp = board[row][col]
            board[row][col] = '#'
            
            if helper(row - 1, col, l + 1) or helper(row + 1, col, l + 1) or helper(row, col - 1, l + 1) or helper(row, col + 1, l + 1):
                return True

            board[row][col] = temp
            
            return False

        for i in range(ROW):
                for j in range(COL):
                    if helper(i,j,0):
                        return True
        return False