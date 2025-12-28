#brute solution
class Solution(object):
    def removeNthFromEnd(self, head):
        temp=head
        stack=[]
        while temp is not None:
            stack.append(temp.val)
            temp=temp.next
        temp=head
        while temp is not None:
            e=stack.pop()
            temp.val=e
            temp=temp.next
        return head


#Optimal Solution
class Solution(object):
    def removeNthFromEnd(self, head):
        curr=head
        prev=None
        while curr is not None:
            front=curr.next
            curr.next=prev
            curr.prev=front
            prev=curr
            curr=front

        return prev


