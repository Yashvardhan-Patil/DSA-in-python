
class Solution(object):
    def hasCycle(self, head):
        tooslow=head
        fast=head
        while fast and fast.next is not None:
            tooslow=tooslow.next
            fast=fast.next.next
            if tooslow==fast:
                return True
        return False
