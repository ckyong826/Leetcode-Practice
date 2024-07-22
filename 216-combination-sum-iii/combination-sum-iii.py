class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def backtrack(comb,SUM,start):
            if start==k and SUM==n:
                res.append(comb)
                return
            elif SUM>n:
                return
            for j in range(1,10):
                if j in comb:
                    break
                backtrack(comb+[j],SUM+j,start+1)
            return res
        return backtrack([],0,0)