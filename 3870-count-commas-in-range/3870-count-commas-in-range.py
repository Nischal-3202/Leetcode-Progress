class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total=0
        start=1000
        while start<=n:
            total+=n-start+1
            start *= 1000
        return total
