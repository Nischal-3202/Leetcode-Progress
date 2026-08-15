class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[0]*(n+1)
        pow=1
        for i in range(1, n+1):
            if (i&(i-1))==0:
                pow=i
            ans[i]=1+ans[i-pow]

        return ans