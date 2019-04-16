class Solution:
    def convert(self, s: str, numRows: int) -> str:
        str_length = len(s)
        node_length = 2*numRows - 2  # 两列之间的差
        result = ""
        if str_length == 0 or numRows == 0 or numRows == 1:
            return s
        for i in range(numRows):  # 从第一行遍历到最后一行
            for j in range(i, str_length, node_length):
                result += s[j]  # 第一行和最后一行  还有普通行的整列数字
                # 非第一行与最末行的，一个周期内，每行有两个元素，所以还有一个元素
                if i != 0 and i != numRows-1 and j - 2*i + node_length < str_length:
                    result += s[j-2*i+node_length]  # 单列行的数字
        return result
