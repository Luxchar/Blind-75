# get length of array, then calculate difference of expected sum vs actual sum

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        actual = sum(nums)
        expected = 0
        for i in range(len(nums)+1):
            expected += i

        return expected - actual
