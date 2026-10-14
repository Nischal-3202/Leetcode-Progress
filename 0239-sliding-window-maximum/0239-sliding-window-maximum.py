class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue=[]
        ans=[]
        for end in range(len(nums)):
            while queue and queue[0] <= end-k:
                queue.pop(0)
            while queue and nums[queue[-1]]< nums[end]:
                queue.pop()
            queue.append(end)
            if end >= k-1:
                ans.append(nums[queue[0]])
        return ans