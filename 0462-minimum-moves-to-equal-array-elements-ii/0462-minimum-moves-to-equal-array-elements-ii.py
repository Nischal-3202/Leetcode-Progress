
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median= nums[len(nums)//2]
        sums=0
        for i in range(len(nums)):
            sums+=abs(nums[i]-median)
        return sums