class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=float('-inf')
        curr_sum=0
        for cur in nums:
            curr_sum = curr_sum+cur
            max_sum=max(max_sum,curr_sum)
            if curr_sum < 0:
                curr_sum=0
        if max_sum < 0:
            return max_sum
        min_sum=float('inf')
        curr_sum=0
        total=0
        for cur in nums:
            total=total+cur
            curr_sum=curr_sum+cur
            min_sum=min(min_sum,curr_sum)
            if curr_sum>0:
                curr_sum=0
        
        return max(max_sum,total-min_sum)