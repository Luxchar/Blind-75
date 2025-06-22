class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # Create dummy node to handle edge case where left = 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node before left position
        for _ in range(left - 1):
            prev = prev.next
        
        # Start reversing from left position
        current = prev.next
        
        # Reverse nodes between left and right
        for _ in range(right - left):
            next_node = current.next
            current.next, next_node.next, prev.next = next_node.next, prev.next, next_node
        
        return dummy.next