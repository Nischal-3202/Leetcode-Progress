class Solution(object):
    def convertdate(self,date):
        days_in_month = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
        month=int(date[:2])
        days=sum(days_in_month[:month-1])
        day=int(date[3:])
        days+=day
        return days

    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        arr1=self.convertdate(arriveAlice)
        arr2=self.convertdate(arriveBob)
        lev1=self.convertdate(leaveAlice)
        lev2=self.convertdate(leaveBob)
        start=max(arr1,arr2)
        end=min(lev1,lev2)
        if end<start:
            return 0
        return end-start+1
                 