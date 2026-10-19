class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        less_count=0
        got_count=0
        for i in range(len(nums)):
            if nums[i]<target:
                less_count+=1
            elif nums[i]== target:
                got_count+=1
        return list(range(less_count,less_count+got_count))