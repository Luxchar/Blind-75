"""Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array."""

def maxProduct(nums):
    for i in range(1,len(nums)):
        nums[i] = max(nums[i]*nums[i-1],nums[i])
        print(nums)
    print(max(nums))

if __name__ == "__main__":
    maxProduct([2,3,-2,4])
    maxProduct([-2,0,-1])