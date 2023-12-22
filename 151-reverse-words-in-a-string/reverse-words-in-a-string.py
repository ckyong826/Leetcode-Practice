class Solution:
    def reverseWords(self, s: str) -> str:
        s+=" "
        string=[]
        j=-1
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                string.append(s[i+1:j])
                j=i
            elif i==0:
                string.append(s[i:j])
        string=[s for s in string if s!=""]
        return ' '.join(string)