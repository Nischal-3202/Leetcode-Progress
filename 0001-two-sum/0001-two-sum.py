class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        i=0
        for num in nums:
            cumilative=target-num
            if cumilative in seen:
                return [seen[cumilative],i]
            seen[num]=i
            i+=1


        