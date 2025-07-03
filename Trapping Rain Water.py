## initialize two pointers left and right
## update 2 variables max left value and max right value on movement
## if the max value is left then move the right pointer and same for the other
## 

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_left, max_right = height[left], height[right]
        total = 0

        if len(height) < 2:
            return 0

        while left < right:
            if max_left > max_right:
                right -=1
                max_right = max(max_right, height[right])
                total += max_right - height[right]
            else:
                left += 1
                max_left = max(max_left, height[left])
                total += max_left - height[left]
        
        return total