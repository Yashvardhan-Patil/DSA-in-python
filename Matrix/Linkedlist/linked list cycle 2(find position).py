class Solution(object):
    def detectCycle(self, head):
        slow=head
        fast=head
        
        while fast and fast.next is not None:
            
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return fast
        return None