class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)-1
        low=0
        high=n
        
        while low < high:
            mid= low + (high-low)/2
            if arr[mid] < arr [mid+1]:
                low=mid+1
            else:
                high=mid
        return low
        