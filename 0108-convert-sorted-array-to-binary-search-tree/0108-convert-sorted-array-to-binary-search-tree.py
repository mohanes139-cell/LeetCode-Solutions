# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

  def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
    def build_bst(left: int, right: int) -> TreeNode | None:
      if left > right:
        return None

      # Always pick the middle element to keep subtrees balanced
      mid = (left + right) // 2
      root = TreeNode(nums[mid])

      # Recursively construct left and right subtrees
      root.left = build_bst(left, mid - 1)
      root.right = build_bst(mid + 1, right)

      return root

    return build_bst(0, len(nums) - 1)