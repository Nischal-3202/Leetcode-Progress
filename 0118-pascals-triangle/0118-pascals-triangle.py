class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[[1]]
        for i in range(1,numRows):
            row=[0]*(i+1)
            row[0],row[i]=1,1
            for j in range(1,i):
                row[j]=ans[i-1][j-1]+ans[i-1][j]
            ans.append(row)
        return ans