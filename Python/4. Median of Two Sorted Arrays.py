class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        com_List = sorted(nums1 + nums2)
        if len(com_List) % 2 != 0:
            pos = int(len(com_List) / 2)
            return float(com_List[pos])
        else:
            pos1 = int(len(com_List) / 2)
            pos2 = pos1 - 1
            return float(com_List[pos1] + com_List[pos2]) / 2
