class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        strs.sort()
        pre=strs[0]
        for i in range(len(pre)):
            for word in strs[1:]:
                if i==len(pre) or pre[i]!=word[i]:
                    return pre[0:i]
        return pre
