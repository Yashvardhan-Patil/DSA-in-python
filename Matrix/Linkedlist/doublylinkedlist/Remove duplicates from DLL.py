class Solution(object):
    def delete(self, head):
        temp=head
        while temp is not None:
            temp=temp.next
            
            if temp.val==temp.prev.val:
                if temp.prev==head:
                    temp.prev=None
                    head=temp
                temp.prev.prev.next=temp
                temp.prev=temp.prev.prev
        return head
