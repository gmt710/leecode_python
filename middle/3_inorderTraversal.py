# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def orderTraversal(self, root, List):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root :
            if root.left:
                self.orderTraversal(root.left, List)
            List.append(root.val)
            if root.right:
                self.orderTraversal(root.right, List)
        return List
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        p = root
        List = []
        if p:
            self.orderTraversal(p, List)
        return List
        
