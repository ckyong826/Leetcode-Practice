class Solution:
    def decodeString(self, s: str) -> str:
        num,temp,ans="","",""
        stack=[]
        for stg in s:
            if stg.isdigit():
                num+=stg
            elif stg.isalpha():
                temp+=stg
            elif stg=="[":
                stack+=[(int(num),temp)]
                temp,num="",""
            elif stg=="]":
                prev_num,prev_txt=stack.pop()
                temp=prev_txt+prev_num*temp
        return temp