class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        min_moves=sum(nums)-n*min(nums)
        return min_moves