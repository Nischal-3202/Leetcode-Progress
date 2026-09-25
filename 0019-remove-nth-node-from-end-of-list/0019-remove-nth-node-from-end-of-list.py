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
        count=0
        temp=head
        while temp!=None:
            temp=temp.next
            count+=1
        count-=n
        if count == 0:
            return head.next
        temp=head
        k=0
        while k<count-1:
            k+=1
            temp=temp.next
        temp.next=temp.next.next
        return head