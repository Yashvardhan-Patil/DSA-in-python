class Solution(object):
    def delete(self, head,key):
        temp=head
        curr=None
        new_node=None
        
        while temp is not None:
            if temp.val==key:
                if curr is not None:
                    curr.next=temp.next
                if temp.next is not None:
                    temp.next.prev=curr
                if temp==new_node:
                    new_node=new_node.next
            curr=temp
            temp=temp.next
        return new_node
            

