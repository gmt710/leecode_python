# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        queue = [root] 
        # 当前遍历层次结点不为空
        while queue:
            # temp存下一层结点
            temp = []
            for x in queue:
                if x:
                    if x.left:
                        temp.append(x.left)
                    if x.right:
                        temp.append(x.right)
            for i,y in enumerate(temp[:-1]):
                y.next = temp[i+1]
            queue = temp
                
