class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        t=s.split(" ")
        return len(t[-1])