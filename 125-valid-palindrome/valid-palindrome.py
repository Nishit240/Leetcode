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
        # s = s.lower()
        # p = s[::-1]

        # if s == p:
        #     return True
        # else:
        #     return False

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


        