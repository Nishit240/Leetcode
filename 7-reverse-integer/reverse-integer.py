# class Solution:
#     def reverse(self, x: int) -> int:
#         # Step 1: Handle the sign and reverse the digits using string slicing
#         sign = -1 if x < 0 else 1
#         res = int(str(abs(x))[::-1]) * sign
        
#         # Step 2: Check for 32-bit integer overflow
#         if res < -2**31 or res > 2**31 - 1:
#             return 0
            
#         return res

class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0
        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10

            if rev < -2**31 or rev > 2**31 - 1:
                return 0
        return sign * rev

        cl