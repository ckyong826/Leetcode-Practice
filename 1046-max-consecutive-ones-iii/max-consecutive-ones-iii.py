class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j=0,0
        index=[]
        ans=0
        maxLength=0
        while i <len(nums):
            if nums[i]==0 and k>0:
                k-=1
                index.append(i)
            elif nums[i]==0:
                index.append(i)
                j=index[0]+1
                index.pop(0)
            i+=1
            ans=i-j
            maxLength=max(maxLength,ans)
        return maxLength
        
