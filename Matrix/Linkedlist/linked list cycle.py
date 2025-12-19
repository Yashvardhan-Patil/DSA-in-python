
class Solution(object):
    def hasCycle(self, head):
        curr=head
        
        visited_position=set()
        while curr is not None:
            if curr in visited_position:
                return True
            visited_position.add(curr)
            curr=curr.next
            
        return False