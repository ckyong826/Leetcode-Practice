class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num={"2":"abc",
             "3":"def",
             "4":"ghi",
             "5":"jkl",
             "6":"mno",
             "7":"pqrs",
             "8":"tuv",
             "9":"wxyz"}
        res=[]
        def backtrack(start,sub):
            if len(sub)==len(digits) :
                res.append(sub[:])
                return
            for i in range(start,len(digits)):
                d=digits[i]
                for j in range(len(num[d])):
                    backtrack(i+1,sub+num[d][j])
        backtrack(0,"")
        return res