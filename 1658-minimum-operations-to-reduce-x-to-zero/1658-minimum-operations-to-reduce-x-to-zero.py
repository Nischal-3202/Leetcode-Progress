class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total=sum(nums)
        target=total-x
        left=0
        current_sum=0
        max_length=-1
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left+=1
            if current_sum == target:
                max_length = max(max_length,right-left+1)
        if max_length==-1:
            return -1
        return len(nums)-max_length