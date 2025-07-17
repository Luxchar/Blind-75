class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
    

    # def myPow      
    #     if n == 0:
    #         return 1
    #     if n < 0:
    #         x = 1/x
    #         n = -n
        
    #     return myPow(x*x, n//2) if n % 2 == 0 else x*myPow(x*x, n//2) 