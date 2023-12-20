class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        temp=money
        temp=temp-prices[0]-prices[1]
        return temp if temp>=0 else money