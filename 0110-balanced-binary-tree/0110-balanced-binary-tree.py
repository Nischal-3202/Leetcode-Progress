# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def height(root):
            if root==None:
                return 0
            left=height(root.left)
            right=height(root.right)
            if left==-1 or right==-1:
                return -1
            if abs(left-right)>1:
                return -1
            return max(left,right)+1

        return height(root)!=-1