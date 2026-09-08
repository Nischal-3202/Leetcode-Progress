class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total=0
        start=1000
        no=1
        while start<=n:
            end=min(n,start*1000-1)
            count=end-start+1
            total += count * no
            start=start*1000
            no+=1
        return total
