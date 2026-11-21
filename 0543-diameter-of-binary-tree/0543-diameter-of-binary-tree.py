# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        global maxDia
        maxDia=0
        def height(root):
            global maxDia
            if root==None:
                return 0
            left=height(root.left)
            right=height(root.right)
            maxDia=max(maxDia,left+right)
            return max(left,right)+1
        height(root)
        return maxDia        