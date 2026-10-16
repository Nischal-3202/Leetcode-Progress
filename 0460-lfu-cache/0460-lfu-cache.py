class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.LRU = Node(0, 0)
        self.MRU = Node(0, 0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
        self.size = 0

    def append(self, node):
        prev=self.MRU.prev
        prev.next=node
        node.prev=prev
        self.MRU.prev=node
        node.next=self.MRU
        self.size+=1
    def remove(self, node):
       prev=node.prev
       nextnode=node.next
       prev.next=nextnode
       nextnode.prev=prev
       self.size-=1
    def pop_lru(self):
        if not self.is_empty():
            popped=self.LRU.next
            self.remove(popped)
            return popped
        else:
            return None  
    
    def is_empty(self):
        return self.size == 0
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.freq = {}
        self.min_freq = 0
    
    def update_frequency(self,node):
        current_freq=node.freq
        freq_list=self.freq[current_freq]
        freq_list.remove(node)
        if freq_list.is_empty() and current_freq==self.min_freq:
            self.min_freq+=1
        node.freq+=1
        if node.freq not in self.freq:
            val=node.freq
            self.freq[val]=DoublyLinkedList()
        self.freq[node.freq].append(node)
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.update_frequency(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity==0:
            return
        if key in self.cache:
            self.cache[key].value=value
            self.update_frequency(self.cache[key])
        else:
            if len(self.cache)>=self.capacity:
                min_list=self.freq[self.min_freq]
                evicted=min_list.pop_lru()
                del self.cache[evicted.key]
            newnode=Node(key,value)
            self.cache[key]=newnode
            if 1 not in self.freq:
                self.freq[1]=DoublyLinkedList()
            self.freq[1].append(newnode)
            self.min_freq=1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)