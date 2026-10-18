# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isMirror(self,L,R):
        if L is None and R is None:
            return True
        if L is None or R is None:
            return False
        if L.val != R.val:
            return False
        return (self.isMirror(L.left, R.right) and
                self.isMirror(L.right, R.left))

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        return self.isMirror(root.left,root.right)