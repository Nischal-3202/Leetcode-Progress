from sortedcontainers import SortedList
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        answer=float("-inf")
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            col_sum=[0]*cols
            for j in range(i,rows):
                for h in range(cols):
                    col_sum[h]=col_sum[h]+matrix[j][h]
                prefix_sum=0
                seen = SortedList([0])
                for l in range(cols):
                    prefix_sum += col_sum[l]
                    need=prefix_sum - k
                    index=seen.bisect_left(need)
                    if index < len(seen):
                        previous_prefix = seen[index]
                        candidate = prefix_sum - previous_prefix
                        answer = max(answer, candidate)
                        if answer == k:
                            return k
                    seen.add(prefix_sum)
        return answer
