class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        for i in range(1,len(matrix)):
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] > target:
                row = i - 1
                break
        if row==-1:
            row= len(matrix) - 1
        start , end = 0, len(matrix[row])
        while start<end:
            mid = (start + end) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                start = mid + 1
            else:
                end = mid
        return False