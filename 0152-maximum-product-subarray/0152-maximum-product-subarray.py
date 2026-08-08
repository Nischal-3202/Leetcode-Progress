class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max,curr_min=1,1
        max_product=float('-inf')
        for num in nums:
            max_pro=curr_max*num
            min_pro=curr_min*num
            curr_max=max(max_pro,num,min_pro)
            curr_min=min(min_pro,num,max_pro)
            max_product=max(curr_max,max_product)
        return max_product