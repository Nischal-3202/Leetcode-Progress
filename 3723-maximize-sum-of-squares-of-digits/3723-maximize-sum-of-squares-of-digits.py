class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        result=""
        if sum==0 or sum>9*num:
            return ""
        while num>0:
            digit=min(9,sum)
            result += str(digit)
            sum -= digit
            num -=1
        return result