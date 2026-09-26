# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(None)
        dummy.next=head
        prev=dummy
        curr=head
        while curr and curr.next:
            if curr.val==curr.next.val:
                while curr.next and curr.val==curr.next.val :
                    curr=curr.next
                prev.next=curr.next
                curr=curr.next
            else:
                prev=curr
                curr=curr.next
        return dummy.next
