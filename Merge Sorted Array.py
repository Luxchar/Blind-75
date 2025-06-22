class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Replace the placeholder zeros with nums2 elements
        nums1[m:] = nums2
        
        # Sort the entire array
        nums1.sort()