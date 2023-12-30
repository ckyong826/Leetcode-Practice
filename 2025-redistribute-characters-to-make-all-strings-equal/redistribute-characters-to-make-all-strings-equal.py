class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        wordSet=defaultdict(int)
        for i in range(len(words)):
            for j in range(len(words[i])):
                wordSet[words[i][j]]+=1
        for k in wordSet:
            if wordSet[k]%len(words)!=0:
                return False
        return True