class Solution:
    def maxScore(self, s: str) -> int:
        score = left = 0
        right = s.count("1")
        for i in range(len(s)-1):
            left += s[i] == "0"
            right -= s[i] == "1"
            score = max(score,left+right)
        return score