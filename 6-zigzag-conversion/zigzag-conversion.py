class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows=[[] for row in range(numRows)]
        i=0
        for c in s:
            rows[i].append(c)
            if i==0:
                step=1
            elif i ==numRows-1:
                step=-1
            i+=step
        for i in range((numRows)):
            rows[i]=''.join(rows[i])
        return ''.join(rows)