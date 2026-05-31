# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        resp = []
        def levelDown(root: Optional[TreeNode], depth: int):
            if root == None:
                return
            if depth+1 > len(resp):
                resp.append([root.val])
            else:
                resp[depth].append(root.val)
            if root.left != None:
                levelDown(root.left, depth+1)
            if root.right != None:
                levelDown(root.right, depth+1)
        
        levelDown(root, 0)
        return resp
        






