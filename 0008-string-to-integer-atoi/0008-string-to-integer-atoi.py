class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        total = 0

        while i < n and s[i].isdigit():
            total = total * 10 + (ord(s[i]) - ord('0'))

            if total * sign > 2147483647:
                return 2147483647

            if total * sign < -2147483648:
                return -2147483648

            i += 1

        return total * sign