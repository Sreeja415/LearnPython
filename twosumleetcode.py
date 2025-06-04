class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  

        for j, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], j]
            num_map[num] = j