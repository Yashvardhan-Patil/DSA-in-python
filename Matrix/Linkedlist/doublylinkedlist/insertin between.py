class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class new:
    def __init__(self):
        self.head = None
    
    def inser(self, val, pos):
        new_node = Node(val)
        
       
        if pos == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            return
        
        curr = self.head
        count = 0
        
        while curr is not None and count < pos - 1:
            curr = curr.next
            count += 1
        
        if curr is None:
            return  
        
        new_node.next = curr.next
        if curr.next is not None:
            curr.next.prev = new_node
        
        curr.next = new_node
        new_node.prev = curr



d1 = new()
d1.inser(5, 0)
d1.inser(10, 1)
print(d1)
