class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row,col=[],[]
        count=0
        for i in range(len(mat)):
            row.append(sum(mat[i]))
        for j in range(len(mat[0])):
            col.append(sum(mat[i][j] for i in range(len(mat))))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1 and row[i]==1 and col[j]==1:
                    count+=1
        return count