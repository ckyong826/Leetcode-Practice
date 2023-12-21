class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        left=0
        right=len(s)-1
        vowel='aeiouAEIOU'
        while left<right:
            if s[left] in vowel and s[right] in vowel:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            elif s[left] not in vowel:
                left+=1
            elif s[right] not in vowel:
                right-=1
        return ''.join(s)