class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        rows=len(matrix)
        cols=len(matrix[0])
        count=0
        for i in range(rows):
            col_sum=[0]*cols
            for j in range(i,rows):
                for k in range(cols):
                    col_sum[k]=col_sum[k]+matrix[j][k]
            #prefixsum method
                prefix_sum=0
                seen_prefix={0:1}
                for l in range(cols):
                    prefix_sum+=col_sum[l]
                    if (prefix_sum-target) in seen_prefix:
                        count+=seen_prefix[prefix_sum-target]
                    if prefix_sum in seen_prefix:
                        seen_prefix[prefix_sum]+=1
                    else:
                        seen_prefix[prefix_sum]=1
        return count