class RecentCounter(object):

    def __init__(self):
        self.queue=[]
        self.result=[]
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        min_admissible=t-3000
        while self.queue and self.queue[0] < min_admissible:
            self.queue.pop(0)
        self.queue.append(t)
        return len(self.queue)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)