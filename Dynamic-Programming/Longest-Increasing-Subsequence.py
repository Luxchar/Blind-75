"""Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7]."""

def lengthofLIS(nums):
    if not nums:
        return 0
    length = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                length[i] = max(length[i], length[j]+1)
    return max(length)

print(lengthofLIS([10,9,2,5,3,7,101,18]))