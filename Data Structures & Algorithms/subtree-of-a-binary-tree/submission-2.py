# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        
        return self.sameTree(root, subRoot) or self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        elif root == None and subRoot != None:
            return False
        elif root != None and subRoot == None:
            return False
        elif root.val != subRoot.val:
            return False
        else:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)  

