# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def treeArr (node: Optional[TreeNode]):
            arr = []
            if node == None:
                return []
            if node.left != None:
                arr.extend(treeArr(node.left))
            else:
                arr.append(-101)
            if node.right != None:
                arr.extend(treeArr(node.right))
            else:
                arr.append(-101)
            
            arr.append(node.val)
            return arr
        pArr = treeArr(p)
        qArr = treeArr(q)
        return pArr == qArr