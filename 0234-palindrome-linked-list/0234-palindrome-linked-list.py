# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if fast != None:
            slow=slow.next
        prev=None
        curr=slow
        while curr:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        while prev:
            if prev.val!=head.val:
                return False
            prev=prev.next
            head=head.next
        return True