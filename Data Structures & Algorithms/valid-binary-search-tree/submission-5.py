# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBstHelper(node, lowerBound, upperBound):
            if node == None:
                return True

            if not(lowerBound < node.val < upperBound):
                return False
            
            return isValidBstHelper(node.left, lowerBound, node.val) and isValidBstHelper(node.right, node.val, upperBound)
        return isValidBstHelper(root, float('-inf'), float('inf'))

