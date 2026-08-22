class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=-1 if x<0 else 1
        x=abs(x)
        ans=int(str(x)[::-1])
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        else:
            return sign*ans