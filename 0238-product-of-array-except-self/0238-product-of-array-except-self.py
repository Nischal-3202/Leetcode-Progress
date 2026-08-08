class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre=[1]*len(nums)
        suf=[1]*len(nums)
        ans=[1]*len(nums)
        for i in range(1,len(nums)):
            pre[i]= pre[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suf[i]=suf[i+1]*nums[i+1]
        for i in range(len(nums)):
            ans[i]=pre[i]*suf[i]
        return ans