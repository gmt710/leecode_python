# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def validBST(self,root,small,large):
        if root==None:
            return True
        if small>=root.val or large<=root.val:
            return False  
        return self.validBST(root.left,small,root.val) and self.validBST(root.right,root.val,large)
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validBST(root,-2**32,2**32-1)
    
            
