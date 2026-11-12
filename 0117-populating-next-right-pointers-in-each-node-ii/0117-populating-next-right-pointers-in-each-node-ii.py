"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        curr = root  # Current node on the parent level
        
        while curr:
            dummy = Node(0)  # Dummy head for the child level
            tail = dummy     # Pointer to build the linked list on the child level
            
            # Traverse the current level using already established `next` pointers
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            
            # Move down to the first node of the newly connected child level
            curr = dummy.next
            
        return root