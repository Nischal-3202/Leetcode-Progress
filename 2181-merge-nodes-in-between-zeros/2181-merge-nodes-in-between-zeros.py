# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sums=0
        curr=head.next
        zeronode=head
        while curr:
            if curr.val:
                sums+=curr.val
            else:
                zeronode.next=curr
                curr.val=sums
                zeronode=curr
                sums=0
            curr=curr.next
        return head.next