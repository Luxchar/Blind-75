# Convert the input array to a set().
# Loop through the numbers in the set.
# if the number does not have a left neighbor (num - 1), it is a starting point.

# once you find a starting point, use a while loop to check if num + 1, num + 2, etc., exist in the set, keeping a count of how long the streak gets.

# Keep track of the maximum streak you find.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n - 1 not in num_set:
                length = 1

                while n + length in num_set:
                    length += 1

                longest = max(longest, length)

        return longest
