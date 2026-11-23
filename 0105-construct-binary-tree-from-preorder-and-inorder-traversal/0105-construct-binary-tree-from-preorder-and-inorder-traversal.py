# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        getpos={}
        i=0
        global idx
        idx=0
        for i in range(len(inorder)):
            getpos[inorder[i]]=i
            i+=1
        def build(left,right):
            if left>right:
                return None
            global idx
            curr=preorder[idx]
            idx+=1
            inorderpos=getpos[curr]
            currNode=TreeNode(curr)
            currNode.left=build(left,inorderpos-1)
            currNode.right=build(inorderpos+1,right)
            return currNode
        return build(0,len(preorder)-1)
        