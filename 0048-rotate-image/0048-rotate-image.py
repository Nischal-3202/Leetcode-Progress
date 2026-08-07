class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            left=0
            right=len(matrix)-1
            while left<right:
                matrix[i][left],matrix[i][right]=matrix[i][right],matrix[i][left]
                left+=1
                right-=1