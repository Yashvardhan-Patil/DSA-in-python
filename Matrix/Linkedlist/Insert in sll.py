class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class sll:
    def __init__(self):
        self.head = None

    def Insert(self,data,position):
        new_node=Node(data)
        if position==0:
            new_node.next=self.head
            self.head=new_node
            return

        else:
            curr=self.head
            pre_Node=None
            count=0
            while curr is not None and count<position:
                pre_Node=curr
                curr=curr.next
                count+=1
            pre_Node.next=new_node
            new_node.next=curr
    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")

obj = sll()

obj.Insert(10, 0)
obj.Insert(20, 1)
obj.Insert(30, 2)
obj.Insert(15, 1)

obj.display()
