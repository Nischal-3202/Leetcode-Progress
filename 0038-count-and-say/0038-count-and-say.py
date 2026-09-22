class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        current='1'
        for _ in range(n-1):
            nextstring=""
            i=0
            while i<len(current):
                digit=current[i]
                count=0
                while i<len(current) and current[i] == digit:
                    count+=1
                    i+=1
                nextstring+=str(count)+digit
            current=nextstring
        return current
