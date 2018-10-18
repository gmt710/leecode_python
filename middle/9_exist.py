class Solution(object):
    # 这题我不会，引用自
    # https://github.com/chenganqi498/leecode/blob/5c0b5cb658a79183c47f8d96cfc03618ddec66df/wordSearch.py
    def search(self, board, word, loc, pointer, tracker): 
        out = False
        directions = [[1,0], [-1,0], [0,1], [0,-1]] 

        # boundary conditions
        if loc[0] == 0:
            directions.remove([-1,0])
        if loc[0] == len(board)-1:
            directions.remove([1,0])
        if loc[1] == 0:
            directions.remove([0,-1])
        if loc[1] == len(board[0]) - 1:
            directions.remove([0,1])

        # 对于满足边界条件的derections，搜索单词
        for [dx, dy] in directions: 
            newtracker = tracker
            newloc = [loc[0]+dx, loc[1]+dy]   
            # 不是之前已经使用过的单元格内的单词，并且找到后面的单词
            if newloc not in tracker and board[newloc[0]][newloc[1]] == word[pointer]:    
                # 将找到的单词位置记录下来
                newtracker = tracker + [newloc]
                # 更新下一个要进行查找的字母位置
                newpointer = pointer + 1  
                # 查找完成后，并且全部找到，就返回True，这里是结束条件
                if newpointer == len(word):
                    return True     
                # 还没找完的话，继续查找
                out = self.search(board, word, newloc, newpointer, newtracker) 
            if out == True:
                break     
        return out
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        pointer = 1
        # board 的行数
        for i in range(len(board)):
            # board 的列数
            for j in range(len(board[0])):
                # 先找到第一个单词的字母
                if board[i][j] == word[0]:
                    # 单词只有一个字母的情况下
                    if len(word) == 1:
                        return True
                    if self.search(board, word, [i,j], pointer, [[i,j]]):
                        return True
        return False

    
