"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        mapping={}
        curr=head
        dummy=Node(0)
        first=0
        prev=dummy
        while curr:
            newcurr=Node(0)
            mapping[curr]=newcurr
            prev.next=newcurr
            prev=newcurr
            curr=curr.next
        curr=head
        mapp=None
        while curr:
            mapp=mapping[curr]
            mapp.val=curr.val
            if curr.next:
                mapp.next=mapping[curr.next]
            if curr.random:
                mapp.random=mapping[curr.random]
            curr=curr.next
        return dummy.next


        