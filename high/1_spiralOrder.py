class Solution(object):    
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 引自https://blog.csdn.net/weixin_41958153/article/details/81141614
        # 设置四种case，观察到第一种case是行不变列一直在变，第二种case的列数不变行数变，以此类推。
        # 并且可以发现规律，第一次遍历的个数等于列数，第二次遍历的个数等于行数减一，
        # 第三次等于列数减一，第四次等于行数再减一
        def cyc(row, column, ri, ci, case):
            """
            :row: 矩阵还有多少行未遍历
            :column: 矩阵还有多少列未遍历
            :ri: 下一次遍历开始时的行
            :ci: 下一次遍历开始时的列
            :case: 是四种情况中的哪一种情况
            """
            # 终止条件
            if (row == 0) or (column == 0):
                return []
            # case 0:遍历次数为列数
            if case == 0:
                # 遍历结束的列：为开始遍历列加上还有多少列未遍历的列数
                endci = ci + column
                for i in range(ci, endci):
                    res.append(matrix[ri][i])
                # 遍历完后，行数比以前少了一行
                row -= 1
                # 下一次遍历，从这一行的下一行开始
                ri += 1
                # range(ci, endci)遍历到的结束一列，应该是(endci-1)，
                # 下一次遍历应该是从(endci-1)开始
                ci = endci - 1
                # 这种情况完成以后，下一次应该是进行(case+1)
                case = (case + 1) % 4
                cyc(row, column, ri, ci, case)

            # case 1:第二次遍历的个数等于行数减一
            elif case == 1:
                # 遍历结束的行：为开始遍历行加上还有多少行未遍历的行数
                endri = ri + row
                for i in range(ri, endri):
                    res.append(matrix[i][ci])
                # 遍历完后，列数比以前少了一列
                column -= 1
                # 下一次遍历，从这一列的上一列开始
                ci -= 1
                # range(ri, endri)遍历到的结束一行，应该是(endri-1)，
                # 下一次遍历应该是从(endri-1)开始
                ri = endri - 1
                # 这种情况完成以后，下一次应该是进行(case+1)
                case = (case + 1) % 4
                cyc(row, column, ri, ci, case)
                
            # case 2:第三次等于列数减一
            elif case == 2:
                # 遍历结束的列：为开始遍历列减去还有多少列未遍历的列数
                endci = ci - column
                for i in range(ci, endci, -1):
                    res.append(matrix[ri][i])
                # 遍历完后，行数比以前少了一行
                row -= 1
                # 下一次遍历，从这一行的上一行开始
                ri -= 1
                # range(ci, endci, -1)遍历到的结束一列，应该是(endci+1)，
                # 下一次遍历应该是从(endci+1)开始
                ci = endci + 1
                # 这种情况完成以后，下一次应该是进行(case+1)
                case = (case + 1) % 4
                cyc(row, column, ri, ci, case)
            
            # case 3:第四次等于行数再减一
            elif case == 3:
                # 遍历结束的行：为开始遍历行减去还有多少行未遍历的行数
                endri = ri - row
                for i in range(ri, endri, -1):
                    res.append(matrix[i][ci])
                # 遍历完后，列数比以前少了一列
                column -= 1
                # 下一次遍历，从这一列的下一列开始
                ci += 1
                # range(ri, endri, -1)遍历到的结束一行，应该是(endri+1)，
                # 下一次遍历应该是从(endri+1)开始
                ri = endri + 1
                # 这种情况完成以后，下一次应该是进行(case+1)
                case = (case + 1) % 4
                cyc(row, column, ri, ci, case)
        res = []
        if len(matrix) == 0:
            return []
        cyc(len(matrix), len(matrix[0]), 0, 0, 0)
        return res
                
        
