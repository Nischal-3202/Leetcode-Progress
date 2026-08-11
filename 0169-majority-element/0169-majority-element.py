class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj_ele=None
        count=0
        for i in range(len(nums)):
            if count == 0:
                maj_ele=nums[i]
            if nums[i]==maj_ele :
                count+=1
            else:
                count -=1
            
        return maj_ele