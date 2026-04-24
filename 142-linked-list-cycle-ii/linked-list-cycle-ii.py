class Solution(object):
    def detectCycle(self, head):
        """
        temp = head
        my_set = set()
        while temp is not None:
            if temp in my_set:
                return temp
            my_set.add(temp)
            temp=temp.next
        return None
        """
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow




         
        