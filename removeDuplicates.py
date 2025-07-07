# create empty array
# for each element in nums
# if its in our array then its already present so skip it
# otherwise add it to our array
# len(our array) is the number of unique element

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = []
        for element in nums:
            if element not in unique_nums:
                unique_nums.append(element)
                # modify nums in place
                nums[nums.index(element)] = element
        return len(unique_nums)