# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

  def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
    if not head:
      return None
    if not head.next:
      return TreeNode(head.val)

    # Use slow and fast pointers to find the middle node.
    # Keep track of 'prev' to split the linked list in half.
    prev = None
    slow = head
    fast = head

    while fast and fast.next:
      prev = slow
      slow = slow.next
      fast = fast.next.next

    # Disconnect the left half from the middle
    if prev:
      prev.next = None

    # Middle node becomes the root
    root = TreeNode(slow.val)

    # Recursively construct left and right subtrees
    root.left = self.sortedListToBST(head)
    root.right = self.sortedListToBST(slow.next)

    return root