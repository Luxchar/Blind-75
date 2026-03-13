class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(matrix)
        rows, cols = len(matrix[0]), len(matrix)

        while left <= right:

            mid = (left+right)//2

            col = mid % cols
            row = mid // rows

            if mid == target:
                return True

            if mid < target:
                left = mid + 1
            else:
                left = mid - 1
        return False
