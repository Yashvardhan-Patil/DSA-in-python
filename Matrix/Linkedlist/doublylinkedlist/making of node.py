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