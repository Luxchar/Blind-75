"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array."""
    
def maxSubArray(nums):
    for i in range(1,len(nums)):
        nums[i] = max(nums[i]+nums[i-1],nums[i])
        print(nums)
    print(max(nums))


if __name__ == "__main__":
    maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    maxSubArray([1])
    maxSubArray([5,4,-1,7,8])