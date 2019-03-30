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
            # 如果是数字的话，就先给num
            if each.isdigit():
                num = 10 *num + int(each)
            # 如果是最后一个数，那么将之间的运算符来计算；如果是运算符，则给pre_op
            if i == len(s) - 1 or each in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop()*num)
                elif pre_op == '/':
                    top = stack.pop()
                    if top < 0:
                        # 如果为-，先取绝对值后再取反
                        stack.append(-(abs(top)//num))
                    else:
                        # 直接取整
                        stack.append(top // num)
                # 如果是运算符，则给pre_op
                pre_op = each
                # 将num赋值为0，用于存下一个数
                num = 0
        
        # 所有的数都是正数的存进去的
        return sum(stack)
            
        
