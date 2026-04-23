# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        length = 0
        temp = head
        while temp is not None:
            length += 1
            temp = temp.next
        
        temp = head
        if length == n:
            new_head = head.next
            del head
            return new_head
        
        temp = head
        node = length - n
        count = 1
        while count < node:
            temp = temp.next
            count += 1
        temp.next = temp.next.next
        return head