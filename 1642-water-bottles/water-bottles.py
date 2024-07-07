class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        while numBottles >= numExchange:
            new_bottles = numBottles // numExchange
            count += new_bottles
            numBottles = new_bottles + (numBottles % numExchange)
        return count