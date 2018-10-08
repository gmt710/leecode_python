# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def LevelOrder(self,root, templist):
        if not root:
            templist.append('#')
        else:
            templist.append(str(root.val))
            self.LevelOrder(root.left, templist)
            self.LevelOrder(root.right, templist)
        return templist
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        templist = []
        self.LevelOrder(root, templist)
        return ','.join(templist)

    def deserializeTree(self, list):
        if len(list)<=0:       
            return None    
        val = list.pop(0)    
        root = None    
        if val != '#':        
            root = TreeNode(int(val))        
            root.left = self.deserializeTree(list)        
            root.right = self.deserializeTree(list)    
        return root
    def deserialize(self, data):
        # split(',')通过指定','分隔符对字符串进行切片
        list = data.split(',')
        return self.deserializeTree(list)

    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
