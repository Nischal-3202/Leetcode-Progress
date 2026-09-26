# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not(head) or not(head.next) or k==0:
            return head

        dummy=head
        curr=head
        count=0
        while curr.next:
            count+=1
            curr=curr.next
        
        no_roto=k%(count+1)
        if no_roto==0:
            return head
        curr.next=head
        no_roto=count-no_roto
        while no_roto>0:
            no_roto-=1
            dummy=dummy.next
        head=dummy.next
        dummy.next=None
        return head
