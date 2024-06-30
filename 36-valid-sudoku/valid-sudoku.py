class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            temp=[num for num in board[i] if num!="."]
            if len(set(temp))!=len(temp):
                return False
            temp=[num[i] for num in board if num[i]!="."]
            if len(set(temp))!=len(temp):
                return False
            if i % 3 == 0:
                for j in range(0, 9, 3):
                    temp = [board[row][col] for row in range(i, i + 3) for col in range(j, j + 3) if board[row][col] != "."]
                    if len(set(temp)) != len(temp):
                        return False
        return True