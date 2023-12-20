class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        temp=money
        temp=temp-sum(prices[:2])
        return temp if temp>=0 else money