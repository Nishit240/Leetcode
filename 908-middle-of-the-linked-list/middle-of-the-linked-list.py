class Solution(object):
    def middleNode(self, head):
        """
        n = 0
        temp = head
        while temp is not None:
            n += 1
            temp = temp.next
            
        temp = head
        for i in range(n//2):
            temp = temp.next
        return temp
        """
        
        slow = head 
        fast = head
        while fast != None and fast.next != None :
            slow = slow.next
            fast = fast.next.next
        return slow 

            




        