# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head
        while curr and curr.next:
            next_node=curr.next
            prev.next=next_node
            curr.next=next_node.next
            next_node.next=curr
            prev=curr
            curr=curr.next
        return dummy.next