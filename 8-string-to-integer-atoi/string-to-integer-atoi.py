class Solution(object):
    def myAtoi(self, s):
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
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i, n = 0, len(s)
        
        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1
        
        # 2. Handle sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # 3. Convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            
            # 4. Overflow check BEFORE multiplying
            if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            
            num = num * 10 + digit
            i += 1
        
        return sign * num


        