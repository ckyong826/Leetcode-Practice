class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=set()
        def helper(temp,start,SUM):
            if SUM==target:
                res.add(tuple(temp))
                return
            elif SUM > target:
                return
            for i in range(start,len(candidates)):
                can=candidates[i]
                if i > start and can == candidates [i-1]:
                    continue
                helper(temp+[can],i+1,SUM+can)
            return [list(sub) for sub in res]
        return helper([],0,0)