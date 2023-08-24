class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
        
            counter_s = [0] * 26
            counter_t = [0] * 26
        
            for char in s:
                counter_s[ord(char) - ord('a')] += 1
        
            for char in t:
                counter_t[ord(char) - ord('a')] += 1
            
            return counter_s == counter_t