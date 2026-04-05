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
    def reverse(self, x: int) -> int:
        if x<=-(1<<31) or x>=(1<<31)-1:
            return 0
            
        if x>0:
            a=int(str(x)[::-1])
            if  a>(1<<31)-1:
                return 0
            return int(str(x)[::-1])
        else:
            a=-int(str(-x)[::-1])
            if a<-(1<<31):
                return 0
            return -int(str(-x)[::-1])