class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        candidates.sort()
        def backtrack(index,remaining,path):
            if remaining==0:
                result.append(path[:])
                return
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>remaining:
                    break
                path.append(candidates[i])
                backtrack(i+1,remaining-candidates[i],path)
                path.pop()
        backtrack(0,target,[])
        return result