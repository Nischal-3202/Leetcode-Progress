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
        curr=head
        dummy=ListNode(0,head)
        mark=dummy
        nodes=[]
        while curr:
            nodes.append(curr)
            curr=curr.next
        length=len(nodes)
        for i in range(length//2):
            dummy.next=nodes[i]
            dummy.next.next=nodes[length-1-i]
            dummy=dummy.next.next
        if length%2 == 1:
            dummy.next=nodes[length//2]
            dummy=dummy.next
        dummy.next=None