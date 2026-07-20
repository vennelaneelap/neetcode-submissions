# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd( self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        # Create a dummy node that points to the original head.
        # This makes removing the first node easier.

        slow = dummy
        # Slow starts at the dummy node.

        fast = dummy
        # Fast also starts at the dummy node.

        for _ in range(n + 1):
            # Move fast n + 1 positions ahead of slow.

            fast = fast.next
            # Move fast forward by one node.

        while fast:
            # Continue until fast moves past the final node.

            slow = slow.next
            # Move slow forward by one node.

            fast = fast.next
            # Move fast forward by one node.

        slow.next = slow.next.next
        # Slow is now directly before the node we need to remove.
        # Skip over that node.

        return dummy.next
        # Return the actual head of the resulting list.