# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head=head
        self.values=[]
        curr=head
        while curr:
            self.values.append(curr.val)
            curr=curr.next
        
    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.values)
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()