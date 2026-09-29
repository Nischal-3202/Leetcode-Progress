# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        curr=head
        values=[]
        while curr:
            values.append(curr.val)
            curr=curr.next
        result=[0]*len(values)
        stack=[]
        for i in range(len(values)):
            while stack and values[i] > values[stack[-1]]:
                popped_index=stack.pop()
                result[popped_index]=values[i]
            stack.append(i)
        return result
                    




