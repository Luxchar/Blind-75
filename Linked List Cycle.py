# loop through the linkedlist
# keep the values seen in the list in an array
# if head.next is None then return false
# if the value has been previously seen in the array then return true

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []
        while head:
            if head not in seen:
                seen.append(head)
            else:
                return True
            head = head.next
        return False
        
        