class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp=""
        l=0
        MAX=0
        i=0
        while i <len(s):
            if s[i] not in temp:
                temp+=s[i]
                l+=1
                i+=1
            else:
                temp=temp[1:]
                l-=1
            MAX=max(l,MAX)
        return MAX
