class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = []
        # 标志位，用于判断是否位偶数位，偶数位由右向左遍历
        flag = 1
        # 当还没遍历完时
        while queue:
            # 用于放每一层的遍历得到的值
            templist = []
            length = len(queue)
            for i in range(length):
                # 先进先出，遍历时还是先左后右，在最后将值颠倒实现偶数层先右后左
                temp = queue.pop(0)
                templist.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            # 一层遍历完，若为偶数层，则将这一层遍历值颠倒
            if flag % 2 == 0:
                templist = templist[::-1]
            res.append(templist)
            flag += 1
        return res
       
