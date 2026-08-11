class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        can_1=None
        can_2=None
        count_1,count1=0,0
        count_2,count2=0,0
        n=len(nums)
        for num in nums:
            if num==can_1:
                count_1+=1
            elif num==can_2:
                count_2+=1
            elif count_1==0:
                can_1=num
                count_1=1
            elif count_2==0:
                can_2=num
                count_2=1
            else:
                count_1-=1
                count_2-=1
        for num in nums:
            if num == can_1:
                count1+=1
            if num == can_2:
                count2+=1
        res=[]
        if count1 > n/3:
            res.append(can_1)
        if count2 > n/3:
            res.append(can_2)
        return res

