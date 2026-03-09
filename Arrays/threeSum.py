# """Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets."""

# def threeSum(nums):
#     if len(nums) != 0:
#         for i in range(2,len(nums)):
#             if nums[i-2] != nums[i-1] and nums[i] != nums[i-2] and nums[i-1] != nums[i] and nums[i-2] + nums[i-1]+nums[i] == 0:
#                 print(nums[i:i+3], end = ", ")
#     print([])


# if __name__ == "__main__":
#     threeSum([-1,0,1,2,-1,-4])
#     threeSum([])
#     threeSum([0])

# either we take an approach with 3 for loops in O(n)3
# or we take a two pointers approach:

# we sort the array to have the nums
# create left = index of a + 1 and right = len(nums)-1
# create an array solutions
# we take "a" which is a number in nums the for a loop will iterate
# for each a, check if left + right + a
# if it is append to solutions array
# return array

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        solutions = set()
        for i in range(len(nums)-1):
            left, right = i+1, len(nums)-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    solutions.add((nums[i], nums[left], nums[right]))
                    left += 1

        return list(solutions)
