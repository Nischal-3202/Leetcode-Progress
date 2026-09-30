class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        sums_map={}
        sums=0
        ans=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sums=nums1[i]+nums2[j]
                if sums in sums_map:
                    sums_map[sums]+=1
                else:
                    sums_map[sums]=1
        
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                sums=nums3[i]+nums4[j]
                if -sums in sums_map:
                    ans+=sums_map[-sums]
        return ans
