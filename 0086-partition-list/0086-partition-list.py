# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummyL=ListNode(0)
        dummyG=ListNode(0)
        curr=head
        currL=dummyL
        currG=dummyG
        while curr:
            if curr.val < x:
                currL.next=curr
                currL=currL.next
            else:
                currG.next=curr
                currG=currG.next
            curr=curr.next
        currG.next=None
        currL.next=dummyG.next
        return dummyL.next
        