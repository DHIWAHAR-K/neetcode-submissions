class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}

        for i, j in enumerate(nums):
            complement = target - j
            if complement in x:
                return [x[complement], i]
            
            x[j] = i