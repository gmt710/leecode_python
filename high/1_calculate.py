class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 思想出自：https://blog.csdn.net/fuxuemingzhu/article/details/80826333
        # 使用的数据结构：堆栈
        # stack = [],stack.append(3),a = stack.pop()
        # 之前的运算符是+，那么需要把之前的数字num进栈，然后等待下一个操作数的到来。 
        # 之前的运算符是-，那么需要把之前的数字求反-num进栈，然后等待下一个操作数的到来。 
        # 之前的运算符是×，那么需要立刻出栈和之前的数字相乘，重新进栈，然后等待下一个操作数的到来。 
        # 之前的运算符是/，那么需要立刻出栈和之前的数字相除，重新进栈，然后等待下一个操作数的到来。
        
        # 初始化一个堆栈,一个符号的,中间值num
        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            if each.isdigit():
                num = 10 *num + int(each)
            if i == len(s) - 1 or each in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop()*num)
                elif pre_op == '/':
                    top = stack.pop()
                    print(top)
                    if top < 0:
                        stack.append(-(abs(top)/num))
                    else:
                        stack.append(top // num)
                        
                pre_op = each
                num = 0
        
        return sum(stack)
            
        
