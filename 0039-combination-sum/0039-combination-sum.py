class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        def backtrack(index,remaining,path):
            if remaining==0:
                result.append(path[:])
                return
            if remaining<0:
                return
            for i in range(index,len(candidates)):
                path.append(candidates[i])
                backtrack(i,remaining-candidates[i],path)
                path.pop()
        backtrack(0,target,[])
        return result