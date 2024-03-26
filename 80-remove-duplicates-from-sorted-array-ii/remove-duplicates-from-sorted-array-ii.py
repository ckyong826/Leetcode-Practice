class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,0
        count=0
        while j<len(nums):
            if nums[i]!=nums[j]:
                i=j
                count+=1
            elif j-i>1:
                nums[j]=float('inf')
            else:
                count+=1
            j+=1
        nums.sort()
        return count
        
