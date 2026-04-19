class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()

        if not s:
            return 0
        i = 0
        sign = 1

        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            i += 1
            sign = -1
        
        p = 0
        while i < len(s):
            cur = s[i]
            if not cur.isdigit():
                break
            else:
                p = p * 10 + int(cur)
            i += 1

        p *= sign

        if p > 2**31 -1:
            return 2**31 -1
        elif p <= -2**31:
            return -2**31
        else:
            return p


        