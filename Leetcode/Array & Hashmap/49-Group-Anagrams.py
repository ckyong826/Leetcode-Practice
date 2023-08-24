class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count=defaultdict(list)
        for a in strs:
            word = ''.join(sorted(a))
            count[word].append(a)
        return list(count.values())