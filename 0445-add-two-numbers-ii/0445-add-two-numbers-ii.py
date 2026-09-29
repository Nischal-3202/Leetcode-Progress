# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse_linked_list(self,head):
        curr=head
        prev=None
        while curr:
            nextval=curr.next
            curr.next=prev
            prev=curr
            curr=nextval
        return prev
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1=self.reverse_linked_list(l1)
        head2=self.reverse_linked_list(l2)
        carry=0
        sums=ListNode(0)
        current=sums
        while head1 or head2 or carry:
            val1=head1.val if head1 else 0
            val2=head2.val if head2 else 0
            total=val1+val2+carry
            digit=total%10
            carry=total//10
            current.next=ListNode(digit)
            current=current.next
            if head1:
                head1=head1.next
            if head2:
                head2=head2.next
        return self.reverse_linked_list(sums.next)