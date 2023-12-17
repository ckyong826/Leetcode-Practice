class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        greatest=max(candies)
        for i in candies:
            can=i+extraCandies
            if can >=greatest:
                result.append(True)
            else:
                result.append(False)
        return result