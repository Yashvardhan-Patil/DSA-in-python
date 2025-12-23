class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
n1=Node(59)
n2=Node(58)
n3=Node(56)
n4=Node(55)

n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3

class makefirsthead:
    def __init__(self):
        self.head=None
    def addathead(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            new_node=self.head

    def append(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
        else:
            curr=self.head
            while curr is not None:
                curr=curr.next
            curr.next=new_node
            new_node.prev=curr
    
    

    
