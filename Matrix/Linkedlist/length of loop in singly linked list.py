
class Solution(object):
    def deleteNode(self, head):
        
        slow=head
        fast=head
        while fast and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                count=0
                slow=slow.next
                while slow!=fast:
                    count+=1
                return count
        return None