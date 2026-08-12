class Solution(object):
    
    def rotate(self, nums, k):
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        cycles = gcd(n,k)
        for i in range(cycles):
            temp=nums[i]
            j=i
            while True:
                a=(j-k+n)%n
                if a==i:
                    break
                nums[j]=nums[a]
                j=a
            nums[j]=temp