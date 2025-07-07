class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:  # Can't reach this position
                return False
            max_reach = max(max_reach, i + nums[i])  # Update furthest reachable
        return max_reach >= len(nums) - 1
    
# Example usage:
solution = Solution()
print(solution.canJump([2,3,1,1,4]))  # Output: True
print(solution.canJump([3,2,1,0,4]))  # Output: False