# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen=set()
        dummy=head
        while dummy:
            if dummy in seen:
                return True
            seen.add(dummy)
            dummy=dummy.next
        return False
        