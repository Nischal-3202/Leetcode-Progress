from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue=deque()
        ans=[]
        for end in range(len(nums)):
            while queue and queue[0] <= end-k:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[end]:
                queue.pop()
            queue.append(end)
            if end >=k-1:
                ans.append(nums[queue[0]])
        return ans
