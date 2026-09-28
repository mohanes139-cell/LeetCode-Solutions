# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        # Dummy node simplifies edge cases where the head changes
        dummy = ListNode(0, head)
        prev = dummy

        # Loop as long as there is a pair of nodes to swap
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # Adjust pointers to swap
            first.next = second.next
            second.next = first
            prev.next = second

            # Move prev to the end of the swapped pair
            prev = first

        return dummy.next