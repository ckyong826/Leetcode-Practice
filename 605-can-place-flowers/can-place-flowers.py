class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        for i in range(len(flowerbed)):
            if i==0 and flowerbed[i]==0 and len(flowerbed)>1 :
                if flowerbed[i+1]==0:
                    flowerbed[i]=1
                    c+=1
            elif i==(len(flowerbed)-1):
                if flowerbed[i]+flowerbed[i-1]==0 :
                    flowerbed[i]=1
                    c+=1
            elif flowerbed[i-1]+flowerbed[i]+flowerbed[i+1]==0:
                flowerbed[i]=1
                c+=1
        return True if n<=c else False
                