"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""

def threeSum(nums):
    if len(nums) != 0:
        for i in range(2,len(nums)):
            if nums[i-2] != nums[i-1] and nums[i] != nums[i-2] and nums[i-1] != nums[i] and nums[i-2] + nums[i-1]+nums[i] == 0:
                print(nums[i:i+3], end = ", ")
    print([])


if __name__ == "__main__":
    threeSum([-1,0,1,2,-1,-4])
    threeSum([])
    threeSum([0])