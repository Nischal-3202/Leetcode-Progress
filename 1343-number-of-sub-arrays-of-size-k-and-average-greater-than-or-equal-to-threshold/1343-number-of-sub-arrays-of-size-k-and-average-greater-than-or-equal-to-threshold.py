class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        window_sum=sum(arr[:k])
        if float(window_sum)/k>=threshold:
            count=1
        else:
            count=0
        for end in range(k,len(arr)):
            window_sum -= arr[end-k]
            window_sum += arr[end]
            if float(window_sum)/k >= threshold:
                count+=1
        return count