class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r=len(matrix)
        c=len(matrix[0])
        left=0
        right=r*c-1 
        while left<=right:
            mid=left+(right-left)//2
            row=mid//c
            column=mid%c
            if matrix[row][column] < target:
                left=mid+1
            elif matrix[row][column] > target:
                right=mid-1
            else:
                return True
        return False
        