class Solution(object):
    def oddEvenList(self, head):
        '''
        if head is None or head.next is None:
            return head 

        values = []
        
        # Collect Odd-indexed nodes (1st, 3rd, 5th...)
        temp = head
        while temp:
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break

        # Collect Even-indexed nodes (2nd, 4th, 6th...)
        temp = head.next
        while temp:
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break
        
        # Re-assign values (This will now have the correct length)
        temp = head
        index = 0
        while temp is not None:
            temp.val = values[index]
            index += 1
            temp = temp.next
        
        return head
        '''
        
        if head is None or head.next is None:
            return head 
        
        odd = head
        even = even_head = head.next

        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return head


