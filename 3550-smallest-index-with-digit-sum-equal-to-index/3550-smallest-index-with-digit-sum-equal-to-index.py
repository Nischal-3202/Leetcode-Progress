class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            sums=0
            for j in str(nums[i]):
                sums+=int(j)
            if sums==i:
                return i
        return -1