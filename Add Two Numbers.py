# make a function that constructs the number from a linkedlist:
# while head, go through each node and multiply the number by the index
# then add the two number and create a linkedlist where we divide the final number for each step

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNumberFromLinkedList(l):
            number = 0
            multiplicator = 1
            while l:
                number += l.val * multiplicator
                multiplicator *= 10
                l = l.next

            return number
        
        total = str(getNumberFromLinkedList(l1) + getNumberFromLinkedList(l2))

        dummy = ListNode(0)
        current = dummy

        for digit in reversed(total):
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next