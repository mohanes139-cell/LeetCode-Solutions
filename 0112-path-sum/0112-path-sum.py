# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        # Base case: empty tree has no paths
        if not root:
            return False
        
        # Check if it is a leaf node
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recurse on left and right subtrees with the reduced sum
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)