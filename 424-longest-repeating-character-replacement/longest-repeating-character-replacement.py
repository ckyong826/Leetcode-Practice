class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char=defaultdict(int)
        aMAX=0
        for c in s:
            char[c]+=1
        for x in char:
            l,r=0,0
            t=k
            MAX=0
            while r < len(s):
                if s[r]!=x and t>0:
                    t-=1
                    r+=1
                elif s[r]!=x and s[l]==x:
                    l+=1
                elif s[r]!=x and s[l]!=x:
                    l+=1
                    t+=1
                else:
                    r+=1
                MAX=max(MAX,r-l)
            aMAX=max(aMAX,MAX)
        return aMAX
                