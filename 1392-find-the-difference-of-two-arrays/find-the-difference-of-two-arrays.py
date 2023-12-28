class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        i,j=set(nums1),set(nums2)
        return [list(i-j),list(j-i)]