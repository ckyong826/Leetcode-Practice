class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp1,temp2=[],[]
        for i in range(m):
            temp1.append(nums1[i])
        for i in range(n):
            temp2.append(nums2[i])
        nums1.clear()
        nums1.extend(temp1)
        nums1.extend(temp2)
        nums1.sort()
        