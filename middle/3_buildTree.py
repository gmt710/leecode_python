# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        # 先序找根结点
        root = TreeNode(preorder[0])
        # 中序找到根节点所在位置，从而找左右子树
        n = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:n+1],inorder[:n])
        root.right = self.buildTree(preorder[n+1:], inorder[n+1:])
        return root
