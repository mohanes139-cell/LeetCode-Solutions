# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []
        
        def dfs(node: TreeNode | None, current_sum: int, path: list[int]):
            if not node:
                return
            
            # Choose: add current node to the path
            path.append(node.val)
            current_sum += node.val
            
            # Check if it is a leaf node and the sum matches targetSum
            if not node.left and not node.right:
                if current_sum == targetSum:
                    result.append(list(path))  # Append a copy of the path
            else:
                # Recurse down children
                dfs(node.left, current_sum, path)
                dfs(node.right, current_sum, path)
            
            # Backtrack: remove current node before returning up the call stack
            path.pop()

        dfs(root, 0, [])
        return result