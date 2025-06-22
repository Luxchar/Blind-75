# go through array
# sort it and then for each number count it until count > n/2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)

        count = 1
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                count+=1
            else:
                count = 1
            
            if count > n/2:
                return nums[i]