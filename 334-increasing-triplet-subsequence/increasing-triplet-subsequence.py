class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minL,maxL=[],[]
        for num in nums:
            if minL and num>minL[-1]:
                minL.append(minL[-1])
            else:
                minL.append(num)
        for num in nums[::-1]:
            if maxL and num<maxL[-1]:
                maxL.append(maxL[-1])
            else:
                maxL.append(num)
        maxL=maxL[::-1]
        for i in range(len(nums)):
            if minL[i]<nums[i]<maxL[i]:
                return True
        return False