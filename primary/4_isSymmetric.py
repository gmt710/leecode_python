# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSametree(self,p,q):
        if not p and not q :
            return True
        if (p and q) and p.val == q.val:
            l = self.isSametree(p.left, q.right)
            r = self.isSametree(p.right, q.left)
            return (l and r)
        else:
            return False
            
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.isSametree(root.left, root.right)

            
        
        
