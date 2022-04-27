class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for idx, value in enumerate(nums):
            if target - value in dict.keys():
                return [dict[target - value], idx]
            else:
                dict[value] = idx
