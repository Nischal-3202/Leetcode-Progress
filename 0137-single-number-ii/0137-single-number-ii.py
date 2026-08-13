class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        for bit in range(32):
            count=0
            for num in nums:
                if num & (1 << bit):
                    count +=1
            if count %3:
                ans= ans | (1 << bit)
            if ans >= ( 1 <<31):
                ans -= (1 << 32)
        return ans