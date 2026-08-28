# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        bstList = []

        def isValidBSTHelper(root: Optional[TreeNode]):
            if root == None:
                return
            elif root.left == None:
                bstList.append(root.val)
                isValidBSTHelper(root.right)
            else:
                isValidBSTHelper(root.left)
                bstList.append(root.val)
                isValidBSTHelper(root.right)
        isValidBSTHelper(root)
        print(bstList)
        
        for i in range(len(bstList)-1):
            if bstList[i] >= bstList[i+1]:
                return False
        return True

