# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 中序遍历二叉搜索树，实际是将其按大小顺序排列
    def inorder(self, root, List):
        if root.left:
            self.inorder(root.left, List)
        List.append(root.val)
        if root.right:
            self.inorder(root.right, List)
        return List
            
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        List = []
        if not root:
            return 0
        List = self.inorder(root, List)
        return List[k-1]
        
        
