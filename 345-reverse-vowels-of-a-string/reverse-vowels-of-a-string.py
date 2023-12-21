class Solution:
    def reverseVowels(self, s: str) -> str:
        temp = [i for i in s if i in "aeiouAEIOU"]
        temp.reverse()
        string=""
        count=0
        for i in s:
            if i in "aeiouAEIOU":
                string+=temp[count]
                count+=1
            else:
                string+=i
        return string