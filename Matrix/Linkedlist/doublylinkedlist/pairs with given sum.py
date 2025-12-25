#brute force
class Solution(object):
    def sum(self, head,target):
        temp1=head
        result=[]
        while temp1 is not None:
            temp2=temp1.next
            while temp2 is not None:
                if temp1.val+temp2.val==target:
                    result.append[[temp1.val,temp2.val]]
                temp2=temp2.next
            temp1=temp1.next
        return result

#Better solution

class Solution(object):
    def sum(self, head,target):
        my_set=set()
        temp=head
        result=[]
        while temp is not None:
            check=target-temp.val
            if check in my_set:
                result.append[[check,temp.val]]
            my_set.add(temp.val)
            temp=temp.next
        return result

#optimal solution
class Solution(object):
    def sum(self, head,target):
        right=head
        result=[]
        while right.next is not None:
            right=right.next
        left=head
        while left<right:
            while left.val+right.val!=target:
                head=head.prev
            result.append[[left.val,right.val]]
            left=left.next
            right=right.prev
        return result