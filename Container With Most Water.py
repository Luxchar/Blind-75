# create var max_size = 0
# create left = 0 and right = len(height)-1
# while left < right
# take the min of the 2 numbers and calculate the max_size based on how much there is between left and right
# store number if max_size is smaller
# return max_size

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_size = 0
        left, right = 0, len(height)-1
        current_size = 0

        while left < right:
            length_container = right - left
            current_size = min(height[left], height[right]) * length_container

            max_size = max(max_size, current_size)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_size
