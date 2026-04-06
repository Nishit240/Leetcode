class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x < 0:
        #     return False
        
        # rev = int(str(x)[::-1])
        
        # if x == rev:
        #     return True
        # else:
        #     return False   

        if x < 0:
            return False
        
        s = str(x)
        return self.helper(s, 0, len(s) - 1)

    def helper(self, s, l, r):
        if l >= r:
            return True
        
        if s[l] != s[r]:
            return False
        
        return self.helper(s, l + 1, r - 1)
        