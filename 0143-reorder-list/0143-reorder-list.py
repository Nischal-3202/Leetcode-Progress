# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        prev=None
        temp1,temp2=ListNode(0),ListNode(0)
        while fast and fast.next:
            prev=slow
            fast=fast.next.next
            slow=slow.next
        if fast != None:
            prev=slow
            slow=slow.next
        prev.next=None
        prev=None
        curr=slow
        while curr:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        first=head
        second=prev
        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2