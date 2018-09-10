# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # if root is None:return []
        # stack = [root]
        # yy=[]
        # #none就出
        # while stack:
        #     y=[]
        #     #出栈
        #     #每一层
        #     print(len(stack))
        #     for i in range(len(stack)):
        #         current = stack.pop(0)
        #         y.append(current.val)
        #         if current.left:
        #         #入栈
        #             stack.append(current.left)
        #         if current.right:  
        #             stack.append(current.right)
        #     yy.append(y)
        # return yy
      
        import Queue
        res = []
        q = Queue.Queue()
        if root:
            q.put(root)
        
        while not q.empty():
            level = []
            length = q.qsize()
            for i in range(length):
                node = q.get()
                level.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            res.append(level)
        return res
    
