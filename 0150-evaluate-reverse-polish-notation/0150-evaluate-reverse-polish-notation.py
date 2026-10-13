class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        operators=['+','-','*','/']
        for c in tokens:
            if c in operators:
                second=stack.pop()
                first=stack.pop()
                if c=='+':
                    stack.append(first + second)
                elif c=='-':
                    stack.append(first - second)
                elif c=='*':
                    stack.append(first * second)
                else:
                    quotient=abs(first)//abs(second)
                    if (first<0) != (second<0):
                        quotient=-quotient
                    stack.append(quotient)
            else:
                stack.append(int(c))
        return stack.pop()