class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<r:
            mid=(l+r)//2
            temp=[ ((p // mid)+(p%mid>0)) for p in piles]
            temp=sum(temp)
            if temp > h:
                l=mid+1
            else:
                r=mid
        return l