

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

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