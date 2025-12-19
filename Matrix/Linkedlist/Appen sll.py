class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class sll:
    
    

    def Append(self,data):
        new_node=Node(data)

        if self.val is None:
            self.val=new_node

        else:
            curr=self.val
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
    def traversal(self):
        if self.val is None:
            print("List is Empty")
        else:
            curr=self.val
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next
            print()
            
    
s=sll()
s.Append(5)
s.Append(55)
s.Append(56)
s.Append(58)

s.traversal()

