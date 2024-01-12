class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1,word2=Counter(word1),Counter(word2)
        if sorted(word1.values())==sorted(word2.values()) and word1.keys() == word2.keys():
            return True
        else: False