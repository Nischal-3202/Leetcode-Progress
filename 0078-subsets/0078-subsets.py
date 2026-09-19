class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subset=[]
        answer=[]
        def backtrack(i):
            if i==len(nums):
                answer.append(subset[:])
                return
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)
        backtrack(0)
        return answer

        