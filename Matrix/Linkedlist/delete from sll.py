class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class sll:
    def __init__(self):
        self.head = None
    def Delete(self,val):
        temp=self.head
        if temp.val==val:
            self.head=temp.next
            del temp
            return
        else:
            found=False
            prev=None
            while temp is not None:
                if temp.val==val:
                    found=True
                    break
                temp=temp.next
                prev=temp
            if found:
                prev.next=temp.next
                return
            else:
                print("Element Not Found")

            
        