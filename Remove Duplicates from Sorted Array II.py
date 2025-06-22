# go through array
# set up count that will reset on number change
# for each number equal add to count
# if count is == 2 then start popping out elements in array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(2, len(nums)):
            if nums[i] == nums[i-2]:
                nums.pop(i)
        return len(nums)