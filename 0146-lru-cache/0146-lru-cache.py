class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.seen={}
        self.LRU=Node()
        self.MRU=Node()
        self.LRU.next=self.MRU
        self.MRU.prev=self.LRU
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.seen:
            node=self.seen[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.seen:
            self.seen[key].value=value
            self.remove(self.seen[key])
            self.insert(self.seen[key])
        else:
            new_node=Node(key,value)
            if len(self.seen)<self.capacity:
                self.insert(new_node)
            else:
                LRU_next=self.LRU.next
                self.remove(LRU_next)
                self.insert(new_node)
                self.seen.pop(LRU_next.key,None)
            self.seen[key]=new_node
    def remove(self,node):
        prev=node.prev
        next_node=node.next
        prev.next=next_node
        next_node.prev=prev
    def insert(self,node):
        prev = self.MRU.prev
        prev.next = node
        node.prev = prev
        node.next = self.MRU
        self.MRU.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)