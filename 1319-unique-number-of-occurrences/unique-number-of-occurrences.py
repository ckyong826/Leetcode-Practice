class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        temp=defaultdict(int)
        for i in range(len(arr)):
            temp[arr[i]] += 1
        temp=sorted(temp.values())
        for i in range(1,len(temp)):
            if temp[i-1]==temp[i]:
                return False
        return True