class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum=0
        count=0
        hash_map={0:1}
        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in hash_map:
                count+=hash_map[prefix_sum-k]
            if prefix_sum in hash_map:
                hash_map[prefix_sum]+=1
            else:
                hash_map[prefix_sum]=1
        return count