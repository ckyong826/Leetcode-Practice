class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count=0
        col,row=defaultdict(int),defaultdict(int)
        n=len(grid)
        temp=[[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                temp[i].append(grid[j][i])
        for k in range(n):
            col[tuple(temp[k])]+=1
            row[tuple(grid[k])]+=1
        for m in col.keys():
            if m in row.keys():
                count+=col[m]*row[m]
        return count