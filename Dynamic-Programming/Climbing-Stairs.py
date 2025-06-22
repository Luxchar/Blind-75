"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def helper(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        
        return helper(n)

