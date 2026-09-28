# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0,head)
        curr=head.next
        prev=head
        while curr:
            nextcurr=curr.next
            search=dummy
            while search.next != curr and search.next.val < curr.val:
                search=search.next
            if search.next != curr:
                prev.next=nextcurr
                temp=search.next
                search.next=curr
                curr.next=temp
            else:
                prev=curr
            curr=nextcurr
        return dummy.next