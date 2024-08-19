from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not (2 <= len(nums) <= 10**4):
            raise ValueError("nums length must be between 2 and 10^4")
        if not (-10**9 <= num <= 10** 9 for num in nums):
            raise ValueError("nums must be between -10^9 and 10^9")
        if not (-10**9 <= target <= 10**9):
            raise ValueError("target must be between -10^9 and 10^9")
        result = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if j != i:
                    defi = nums[i]
                    defj = nums[j]
                    a = defi + defj
                    if a == target:
                        result.append(i)
                        result.append(j)
        return result
