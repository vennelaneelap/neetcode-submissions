# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # If the list has zero or one node, no reordering is needed.
        if not head or not head.next:
            return

        # Both pointers begin at the first node.
        slow = head
        fast = head

        # Move slow one step and fast two steps.
        # When fast reaches the end, slow reaches the middle.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # The second half starts after slow.
        second = slow.next

        # Disconnect the first half from the second half.
        slow.next = None

        # Previous starts as None because the new tail points to None.
        previous = None

        # Current starts at the beginning of the second half.
        current = second

        # Reverse the second half.
        while current:

            # Save the next node before changing the pointer.
            next_node = current.next

            # Reverse the current node's pointer.
            current.next = previous

            # Move previous forward.
            previous = current

            # Move current forward using the saved pointer.
            current = next_node

        # Previous is now the head of the reversed second half.
        second = previous

        # First starts at the beginning of the first half.
        first = head

        # Merge the first and second halves alternately.
        while second:

            # Save the next node in the first half.
            first_next = first.next

            # Save the next node in the second half.
            second_next = second.next

            # Connect the current first-half node to the second-half node.
            first.next = second

            # Connect the second-half node to the next first-half node.
            second.next = first_next

            # Move first forward.
            first = first_next

            # Move second forward.
            second = second_next