class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s=list(s)
        for i in range(len(t)-1,-1,-1):
            if s and t[i]==s[-1]:
                s.pop(-1)
        if s==[]:
            return True
        else:
            return False