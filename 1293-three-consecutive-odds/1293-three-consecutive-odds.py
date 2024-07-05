class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count=0
        cons=False
        for num in arr:
            if num%2==1 and cons:
                count+=1
            elif num%2==1:
                cons=True
                count+=1
            else:
                cons=False
                count=0
            if count>=3:
                return True
        return False