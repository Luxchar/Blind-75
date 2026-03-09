# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         cleaned = "".join(c.lower() for c in s if c.isalnum())
#         return cleaned == cleaned[::-1]

# 2 pointers solution:
# left=0 right=len of s
# check if left and right are valid letters or numbers
# compare them and if they're not same, return False
# otherwise return true if left > right
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1

        while left < right:
            # check if left and right are alphanumeric
            if s[left].isalnum() == False:
                left += 1
                continue
            if s[right].isalnum() == False:
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
