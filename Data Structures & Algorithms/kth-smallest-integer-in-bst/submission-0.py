# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def getSmallest(curr: TreeNode) -> (int, TreeNode):
            if curr.left == None:
                val = curr.val
                root = curr.right
                return val, root

            smallestNode = curr.left
            prev = curr

            while smallestNode.left != None:
                prev = smallestNode
                smallestNode = smallestNode.left
            val = smallestNode.val
            prev.left = smallestNode.right
            return val, curr
        
        for i in range(0, k):
            print(i)
            print(root.val)
            if i == k-1:
                val, _ = getSmallest(root)
                return val
            else:
                _, root = getSmallest(root)
        return 0

