class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList(object):

    def __init__(self):
        self.head=None
        self.size=0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index <0 or index >=self.size:
            return -1
        curr=self.head
        for i in range(index):
            curr=curr.next
        return curr.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newnode=Node(val)
        newnode.next=self.head
        self.head=newnode
        self.size+=1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newnode=Node(val)
        if self.head is None:
            self.head=newnode
            self.size+=1
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=newnode
        self.size+=1
        
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index <0 or index > self.size:
            return
        if index==0:
            self.addAtHead(val)
            return
        prev=self.head
        for i in range(index-1):
            prev=prev.next
        newnode=Node(val)
        newnode.next=prev.next
        prev.next=newnode
        self.size+=1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index<0 or index>=self.size:
            return
        if index==0:
            self.head=self.head.next
            self.size-=1
            return
        prev=self.head
        for i in range(index-1):
            prev=prev.next
        prev.next=prev.next.next
        self.size -=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)