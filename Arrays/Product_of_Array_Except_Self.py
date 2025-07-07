"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]."""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        # Left pass
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]
        
        # Right pass
        right = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result