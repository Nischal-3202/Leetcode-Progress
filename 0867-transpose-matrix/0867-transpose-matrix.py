class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(matrix)
        n=len(matrix[0])
        transpose=[[matrix[i][j] for i in range(m)] for j in range(n)]
        return(transpose)