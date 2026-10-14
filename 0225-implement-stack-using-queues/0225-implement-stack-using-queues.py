class MyStack(object):

    def __init__(self):
        self.queue=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()