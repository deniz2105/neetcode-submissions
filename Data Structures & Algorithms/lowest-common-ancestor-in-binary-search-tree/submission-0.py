# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def path(r: TreeNode, target: TreeNode)->List[TreeNode]:
            if r == None:
                return []
            resp = []
            resp.append(r)
            if r.val == target.val:
                return resp
            if r.val > target.val:
                resp.extend(path(r.left, target))
                return resp
            
            resp.extend(path(r.right, target))
            return resp
                
        pPath = path(root, p)
        qPath = path(root, q)

        minLen = min(len(pPath), len(qPath))
        for a in pPath:
            print( a.val)
        print("next")
        for a in qPath:
            print( a.val)
        for i in range(0, minLen-1):
            if pPath[i+1] != qPath[i+1]:
                return pPath[i]
        if minLen == len(pPath):
            return pPath[minLen-1]
        else:
            return qPath[minLen-1]
