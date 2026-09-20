class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        for i in range(len(s)):
            value=26-(ord(s[i])-ord('a'))
            sum+=(i+1)*value
        return sum