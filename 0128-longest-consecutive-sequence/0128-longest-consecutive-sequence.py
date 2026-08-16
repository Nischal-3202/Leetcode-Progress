class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set=set(nums)
        count=0
        for i in nums_set:
            
            if i-1 not in nums_set:
                curr_count=1
                j=i
                while j+1 in nums_set:
                    curr_count+=1
                    j+=1
                count=max(count,curr_count)
        return count