"""
Sliding window approach:
- Use two pointers (left and right) to maintain a window
- Use a set or hashmap to track characters in current window
- Expand window by moving right pointer
- When duplicate found, shrink window from left until no duplicates
- Track maximum window size seen so far
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If character is already in window, shrink from left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character to window
            char_set.add(s[right])
            
            # Update maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length