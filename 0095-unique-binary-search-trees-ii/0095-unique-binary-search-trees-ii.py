# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

  def generateTrees(self, n: int) -> list[TreeNode | None]:
    if n == 0:
      return []

    memo = {}

    def build_trees(start: int, end: int) -> list[TreeNode | None]:
      if start > end:
        return [None]

      if (start, end) in memo:
        return memo[(start, end)]

      all_trees = []

      for val in range(start, end + 1):
        # Generate all left and right subtrees
        left_subtrees = build_trees(start, val - 1)
        right_subtrees = build_trees(val + 1, end)

        # Connect left and right subtrees to the root
        for left in left_subtrees:
          for right in right_subtrees:
            root = TreeNode(val)
            root.left = left
            root.right = right
            all_trees.append(root)

      memo[(start, end)] = all_trees
      return all_trees

    return build_trees(1, n)