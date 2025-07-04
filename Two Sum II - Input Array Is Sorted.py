## create 2 variable left and right
## if left + right is below target, move left to the right +1
## if its above target move right to the left -1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        total = numbers[left] + numbers[right]

        while total != target:
            if total > target:
                right -= 1
            else:
                left += 1
            total = numbers[left] + numbers[right]

        return [left+1, right+1]