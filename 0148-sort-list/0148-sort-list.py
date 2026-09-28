# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            prev=slow
            fast=fast.next.next
            slow=slow.next
        if fast != None:
            prev=slow
            slow=slow.next
        prev.next=None
        left_sorted=self.sortList(head)
        right_sorted=self.sortList(slow)
        return self.merge(left_sorted,right_sorted)
    
    def merge(self,left,right):
        dummy=ListNode(0)
        pointer=dummy
        while left and right:
            if left.val < right.val:
                dummy.next=left
                dummy=dummy.next
                left=left.next
            else:
                dummy.next=right
                dummy=dummy.next
                right=right.next
        dummy.next=left if left else right
        return pointer.next
        