class Solution(object):
    def calculate(self, s):
        def priority(op):
            if op == '*' or op == '/':
                return 2
            return 1

        number_stack = []
        operator_stack = []
        i = 0

        while i < len(s):
            c = s[i]

            if c == ' ':
                i += 1
                continue

            if c.isdigit():
                num = 0

                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                number_stack.append(num)
                continue

            else:
                while (operator_stack and
                       priority(operator_stack[-1]) >= priority(c)):

                    op = operator_stack.pop()
                    second = number_stack.pop()
                    first = number_stack.pop()

                    if op == '+':
                        number_stack.append(first + second)
                    elif op == '-':
                        number_stack.append(first - second)
                    elif op == '*':
                        number_stack.append(first * second)
                    else:
                        quotient = abs(first) // abs(second)

                        if (first < 0) != (second < 0):
                            quotient = -quotient

                        number_stack.append(quotient)

                operator_stack.append(c)

            i += 1

        # Evaluate remaining operators AFTER processing the entire string
        while operator_stack:
            op = operator_stack.pop()
            second = number_stack.pop()
            first = number_stack.pop()

            if op == '+':
                number_stack.append(first + second)
            elif op == '-':
                number_stack.append(first - second)
            elif op == '*':
                number_stack.append(first * second)
            else:
                quotient = abs(first) // abs(second)

                if (first < 0) != (second < 0):
                    quotient = -quotient

                number_stack.append(quotient)

        return number_stack[-1]