# if len array is < 3 return []
# loop through array with bounds 0, len(array)-2
# check all conditions
# if a triplet is found, add it to the array if its not already in it

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        triplets = []
        
        for i in range(len(nums) - 2):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # j starts after i, k starts at the end
            j = i + 1  # left pointer
            k = len(nums) - 1  # right pointer
            
            while j < k:  # Instead of nested loops, we move pointers
                current_sum = nums[i] + nums[j] + nums[k]
                
                if current_sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    
                    # Skip duplicates for j and k
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    j += 1  # Move both pointers
                    k -= 1
                elif current_sum < 0:
                    j += 1  # Need larger sum, move left pointer right
                else:
                    k -= 1  # Need smaller sum, move right pointer left
        
        return triplets

    
if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([0, 0, 0]))
    print(s.threeSum([1, 2, -2, -1]))
    print(s.threeSum([]))
    print(s.threeSum([3, 0, -4, -1, -2, 1, 2]))