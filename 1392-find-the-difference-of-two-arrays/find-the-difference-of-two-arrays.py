class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        DA,DB=defaultdict(),defaultdict()
        ans=[]
        for i in range(len(nums1)):
            DA[nums1[i]]=1
        for i in range(len(nums2)):
            DB[nums2[i]]=1
        for j in range(len(nums1)):
            if nums1[j] in DB.keys():
                DB.pop(nums1[j])
        for j in range(len(nums2)):
            if nums2[j] in DA.keys():
                DA.pop(nums2[j])
        ans.append(DA.keys())
        ans.append(DB.keys())
        return ans