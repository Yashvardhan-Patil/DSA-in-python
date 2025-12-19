class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

node1=Node(5)
node2=Node(6)
node3=Node(9)
node4=Node(4)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=None

print(node1.next.val)


