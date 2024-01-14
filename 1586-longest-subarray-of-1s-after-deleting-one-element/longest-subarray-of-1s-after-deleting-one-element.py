class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxLength=0
        temp=0
        count=0
        index=[]
        if sum(nums)==len(nums):
            return len(nums)-1
        for i in range(len(nums)):
            if nums[i]==0 and count==2:
                num=temp
                temp-=sum(nums[index[-2]:index[-1]])
                maxLength=max(maxLength,num,temp)
                index.append(i)
            elif nums[i]==0 and count==1:
                maxLength=temp
                temp-=sum(nums[:index[-1]])
                maxLength=max(maxLength,temp)
                count+=1
                index.append(i)
            elif nums[i]==0:
                count+=1
                index.append(i)
            else:
                temp+=nums[i]
        maxLength=max(maxLength,temp)
        return maxLength