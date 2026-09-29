# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prefix_sum={}
        prefix=0
        dummy=ListNode(0,head)
        curr=dummy
        while curr:
            prefix+=curr.val
            prefix_sum[prefix]=curr
            curr=curr.next
        prefix=0
        curr=dummy
        while curr:
            prefix+=curr.val
            curr.next=prefix_sum[prefix].next
            curr=curr.next
        return dummy.next