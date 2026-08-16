class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """Combinations methods"""
        def fact(n):
            if n==0:
                return 1
            return n*fact(n-1)
        down=m-1
        across=n-1
        return (fact(down+across)/(fact(down)*fact(across)))
        
        