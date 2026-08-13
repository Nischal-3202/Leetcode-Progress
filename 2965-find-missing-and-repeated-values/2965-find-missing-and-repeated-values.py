class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        sums=0
        sqr_sum=0
        n=len(grid)*len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sums += grid[i][j]
                sqr_sum += grid[i][j] ** 2
        pure_sum= n*(n+1)//2
        pure_sum_square=n*(n+1)*(2*n+1)//6
        sqr_diff=sqr_sum-pure_sum_square
        diff=sums-pure_sum
        x=((sqr_diff//diff)+diff)//2
        y=x-diff
        return [x,y]
