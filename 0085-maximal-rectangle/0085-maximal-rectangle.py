class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_area=float('-inf')
        rows=len(matrix)
        cols=len(matrix[0])
        for top in range(rows):
            col_sum=[0]*cols
            for bottom in range(top,rows):
                for col in range(cols):
                    col_sum[col]= col_sum[col] + int(matrix[bottom][col])
                curr_sum=0
                for col in range(cols):
                    if col_sum[col] == (bottom-top+1):
                        curr_sum+=1
                    else:
                        curr_sum=0
                    max_area=max(max_area,curr_sum*(bottom-top+1))
        return max_area