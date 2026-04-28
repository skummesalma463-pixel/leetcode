class Solution:
    def isBalanced(self, root):
        
        def checkHeight(node):
            if not node:
                return 0
            
            left = checkHeight(node.left)
            if left == -1:
                return -1
            
            right = checkHeight(node.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        
        return checkHeight(root) != -1