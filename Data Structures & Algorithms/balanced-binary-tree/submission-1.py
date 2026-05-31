# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root:  Optional[TreeNode])-> int:
            if root == None:
                return 0
            rightDepth  = depth(root.right)
            leftDepth  = depth(root.left)
            if root.left == None and root.right != None:
                return max(leftDepth, rightDepth+1)
            elif root.left != None and root.right == None:
                return max(leftDepth+1, rightDepth)
            return max(leftDepth+1, rightDepth+1)
        if root == None:
            return True
        depthLeft = depth(root.left)
        depthRight = depth(root.right)
        print(depthLeft)
        print(depthRight)
        if abs(depthLeft-depthRight) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
            
