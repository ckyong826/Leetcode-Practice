class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2)>len(nums1):
            temp=nums2
            nums2=nums1
            nums1=temp
        nums1.sort()
        nums2.sort()
        i=0
        result=[]
        while i < len(nums1):
            if nums1[i] in nums2:
                result.append(nums1[i])
                nums2.remove(nums1[i])
            i+=1
        return result
            