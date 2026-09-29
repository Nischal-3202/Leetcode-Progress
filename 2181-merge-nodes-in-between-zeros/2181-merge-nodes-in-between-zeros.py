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
        dummy=ListNode(0)
        dummyhead=dummy
        curr=head.next
        sums=0
        zero_seen=False
        while curr:
            if curr.val != 0:
                sums += curr.val
            else:
                newnode=ListNode(sums)
                dummyhead.next=newnode
                dummyhead=dummyhead.next
                sums=0
            curr=curr.next
        return dummy.next