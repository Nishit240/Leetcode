class Solution(object):
    def removeNthFromEnd(self, head, n):
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
        """
        
        slow = fast = head

        for _ in range(n):
            fast = fast.next

        if fast == None:
            return head.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
        return head

         