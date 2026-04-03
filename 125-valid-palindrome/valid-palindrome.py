class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # if s == " ":
        #     return True
        
        # s = s.replace(" ", "")
        # s = s.replace(",", "")
        # s = s.replace(":", "")

        # if s.lower() == s[::-1].lower():
        #     return True
        # else:
        #     return False

        s= ''.join([char for char in s if char.isalnum()])
        if s[::-1].lower() == s.lower():
            return True 
        return False 


        