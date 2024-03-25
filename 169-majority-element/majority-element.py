class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        table=defaultdict(int)
        LEN=len(nums)/2
        for num in nums:
            table[num]+=1
        for num in table:
            if table[num]>LEN:
                return num