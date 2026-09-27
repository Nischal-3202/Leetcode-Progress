# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0,head)
        curr=head
        length=0
        while curr:
            curr=curr.next
            length+=1
        groups=length//k
        curr=head
        before=dummy
        while groups>0:
            start=curr
            prev=None
            for _ in range(k):
                nextnode=curr.next
                curr.next=prev
                prev=curr
                curr=nextnode
            before.next=prev
            start.next=curr
            before=start
            groups-=1
        return dummy.next
        