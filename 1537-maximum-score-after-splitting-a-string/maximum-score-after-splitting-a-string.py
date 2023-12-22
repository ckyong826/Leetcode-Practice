class Solution:
    def maxScore(self, s: str) -> int:
        score=0
        for i in range(len(s)-1):
            newScore=0
            left=s[:i+1]
            right=s[i+1:]
            for j in left:
                if j=="0":
                    newScore+=1
            for l in right:
                if l=="1":
                    newScore+=1
            score=max(score,newScore)
        return score