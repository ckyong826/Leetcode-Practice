class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        count=1
        rev=False
        for i in range(time):
            if rev == True and count>1:
                count -=1
            elif rev == True:
                rev = False
                count += 1
            elif count == n:
                rev = True
                count -=1
            else:
                count += 1
        return count