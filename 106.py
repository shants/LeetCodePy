# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if len(inorder)==0:
            return None

        idx = inorder.index(postorder[-1])
        postorder.pop()
        t = TreeNode(inorder[idx])
        t.left = self.buildTree(inorder[:idx], postorder)
        t.right = self.buildTree(inorder[idx+1:],postorder)
        return t