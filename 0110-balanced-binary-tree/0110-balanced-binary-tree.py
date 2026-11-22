class Solution(object):
    def isBalanced(self, root):

        def height(root):
            if root == None:
                return 0

            return max(height(root.left), height(root.right)) + 1

        if root == None:
            return True

        left = height(root.left)
        right = height(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)