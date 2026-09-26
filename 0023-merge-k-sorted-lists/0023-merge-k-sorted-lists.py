# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        result=ListNode(0)
        curr=result
        pointers=[0]*len(lists)
        for i in range(len(lists)):
            pointers[i]=lists[i]
        while True:
            min_index=-1
            for i in range(len(pointers)):
                if pointers[i] is not None:
                    if min_index==-1 or pointers[i].val < pointers[min_index].val:
                        min_index=i
            if min_index==-1:
                break
            curr.next=pointers[min_index]
            curr=curr.next
            pointers[min_index]=pointers[min_index].next
        return result.next
        