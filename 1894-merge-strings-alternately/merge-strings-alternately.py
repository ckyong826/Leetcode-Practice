class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length=len(word1)
        merge=""
        if len(word2)>length:
            length=len(word2)
        for i in range(length):
            if i<len(word1):
                merge+=word1[i]
            if i<len(word2):
                merge+=word2[i]
        return merge