class Solution(object):
    def calculate(self, s):
        total = 0
        last_num = 0
        num = 0
        sign = '+'

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)

            if (not c.isdigit() and c != ' ') or i == len(s) - 1:
                if sign == '+':
                    total += last_num
                    last_num = num

                elif sign == '-':
                    total += last_num
                    last_num = -num

                elif sign == '*':
                    last_num *= num

                elif sign == '/':
                    quotient = abs(last_num) // abs(num)
                    if (last_num < 0) != (num < 0):
                        quotient = -quotient
                    last_num = quotient

                sign = c
                num = 0

        return total + last_num