# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        resp = []
        if root == None:
            return resp
        
        if root.left != None:
            resp.extend(self.postorderTraversal(root.left))
        if root.right != None:
            resp.extend(self.postorderTraversal(root.right))
        
        resp.append(root.val)

        return resp