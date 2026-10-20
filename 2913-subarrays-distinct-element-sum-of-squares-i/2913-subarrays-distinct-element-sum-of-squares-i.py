class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        for i in range(len(nums)):
            sets=set()
            for j in range(i,len(nums)):
                sets.add(nums[j])
                total+=len(sets)**2
        return total