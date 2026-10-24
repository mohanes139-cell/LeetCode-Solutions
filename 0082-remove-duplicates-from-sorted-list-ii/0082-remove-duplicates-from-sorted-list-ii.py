# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy
        
        while head:
            # Check if current node is the start of duplicates
            if head.next and head.val == head.next.val:
                # Move head forward until the end of the duplicate run
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skip all duplicate nodes
                prev.next = head.next
            else:
                # No duplicate for current node, advance prev
                prev = prev.next
                
            head = head.next
            
        return dummy.next