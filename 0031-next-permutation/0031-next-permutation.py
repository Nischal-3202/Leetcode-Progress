class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        brk=-1
        swap_i=-1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                brk=i
                break
        if brk==-1:
            nums.reverse()
            return
        
        for i in range(n-1,brk,-1):
            if nums[i] > nums[brk]:
                swap_i=i
                break
        
        nums[brk],nums[swap_i]=nums[swap_i],nums[brk]

        nums[:]=nums[:brk+1]+nums[:brk:-1]
        



