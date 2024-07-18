class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def helper(start,SUM,temp):
            if SUM==target:
                res.append(temp[:])
            elif SUM < target:
                for i in range(start,len(candidates)):
                    helper(i,SUM+candidates[i],temp+[candidates[i]])
            return res
        return helper(0,0,[])
            
