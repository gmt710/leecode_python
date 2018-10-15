class Solution(object):
    def fuhao(self, fuhao, a,b):
        a,b = int(a),int(b)
        if fuhao == "+":
            return a+b
        if fuhao == "-":
            return a-b
        if fuhao == "*":
            return a*b
        if fuhao == "/":
            # 除法的符号
            flag = -1 if (a<0) ^ (b<0) else 1
            return flag*(abs(a)//abs(b))
    
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        fuhao = ["+","-","*","/"]
        i = 0
        while i < len(tokens):
            # 如果是符号的话，就进行运算
            if tokens[i] in fuhao:
                # 对应的符号进行运算
                tokens[i-2] = self.fuhao(tokens[i],tokens[i-2], tokens[i-1])
                del tokens[i-1]
                del tokens[i-1]
                i = i - 2
            i += 1
        return int(tokens[0])
