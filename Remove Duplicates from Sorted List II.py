# make an array that store unique values
# loop through linkedlist, if the value is already seen, set prev.next to current.next and keep going on current.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head:
            if head.next and head.val == head.next.val:
                val = head.val
                while head and head.val == val:
                    head = head.next
                prev.next = head
            else:
                prev = head
                head = head.next

        return dummy.next