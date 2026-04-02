class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        rev = int(str(x)[::-1])
        
        if x == rev:
            return True
        else:
            return False        