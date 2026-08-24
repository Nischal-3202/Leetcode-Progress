class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if (dividend < 0) != (divisor < 0):
            sign = -1
        else:
            sign = 1
        dividend=abs(dividend)
        divisor=abs(divisor)
        answer = 0
        while dividend >= divisor:
            current = divisor
            multiple = 1
            while current + current <= dividend:
                current = current + current
                multiple = multiple + multiple
            dividend = dividend - current
            answer = answer + multiple
        if sign == -1:
            answer = -answer
        return answer

        
            
        