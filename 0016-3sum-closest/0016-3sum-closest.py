class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_gap=float('inf')
        ans=0
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            L=i+1
            R=len(nums)-1
            while L<R:
                sum=nums[i]+nums[L]+nums[R]
                
                if abs(target-sum) < min_gap:
                    min_gap=abs(sum-target)
                    ans=sum
                if sum < target:
                    L+=1
                elif sum > target:
                    R-=1
                else:
                    return target
        return ans
                
            
