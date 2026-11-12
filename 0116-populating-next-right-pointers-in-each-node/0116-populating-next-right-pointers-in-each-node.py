class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        leftmost = root
        
        # Since it's a perfect binary tree, if leftmost.left exists, 
        # there is another level below to connect.
        while leftmost.left:
            head = leftmost
            
            while head:
                # Connection 1: Connect children of the same parent
                head.left.next = head.right
                
                # Connection 2: Connect right child to the next parent's left child
                if head.next:
                    head.right.next = head.next.left
                
                # Move to the next node on the current level
                head = head.next
            
            # Move down to the start of the next level
            leftmost = leftmost.left
            
        return root