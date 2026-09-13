class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                result.extend(intervals[intervals.index(interval):])
                return result
            else:
                newInterval[0]=min(interval[0],newInterval[0])
                newInterval[1]=max(interval[1],newInterval[1])
        result.append(newInterval)
        return result