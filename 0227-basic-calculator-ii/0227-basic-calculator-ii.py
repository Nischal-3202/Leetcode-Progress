class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        sign = '+'

        for i in range(len(s)):
            c = s[i]

            if c.isdigit():
                num = num * 10 + int(c)

            if (not c.isdigit() and c != " ") or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)

                elif sign == '-':
                    stack.append(-num)

                elif sign == '*':
                    stack.append(stack.pop() * num)

                elif sign == '/':
                    top = stack.pop()
                    quotient = abs(top) // abs(num)

                    if (top < 0) != (num < 0):
                        quotient = -quotient

                    stack.append(quotient)

                sign = c
                num = 0

        return sum(stack)