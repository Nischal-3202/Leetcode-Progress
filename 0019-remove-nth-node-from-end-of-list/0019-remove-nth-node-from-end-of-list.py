# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        temp1 = head
        temp2 = head
        for i in range(n):
            temp2 = temp2.next
        if temp2 == None:
            return head.next
        while temp2.next != None:
            temp1 = temp1.next
            temp2 = temp2.next
        temp1.next = temp1.next.next
        return head