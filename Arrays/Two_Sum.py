"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""
    
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return [i, j]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store value -> index mapping
        num_map = {}
        
        for i, num in enumerate(nums): # Enumerate gives us both index and value eg # (0, 2), (1, 7), (2, 11), (3, 15)
            complement = target - num # Calculate the complement needed to reach the target eg 9 - 2 = 7
            
            # Check if complement exists in our map eg if 7 exists in {2: 0, 7: 1, 11: 2, 15: 3}
            if complement in num_map:
                return [num_map[complement], i] # eg [1, 0] for input (2, 7)

            # Store current number and its index
            num_map[num] = i # eg {2: 0, 7: 1, 11: 2, 15: 3}
        
        # This should never be reached given the problem constraints
        return []

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15],9))
    print(s.twoSum([3,2,4],6))
    print(s.twoSum([3,3],6))