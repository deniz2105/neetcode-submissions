# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        resp = [root.val]
        if root.left != None:
            resp.extend(self.preorderTraversal(root.left))
        if root.right != None:
            resp.extend(self.preorderTraversal(root.right))
        return resp
