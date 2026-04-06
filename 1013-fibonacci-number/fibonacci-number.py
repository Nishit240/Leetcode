class Solution:

    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        else:
            result = self.fib(n-1) + self.fib(n-2)
        return result

        # a,b=0,1
        # for i in range(n):
        #     a,b=b,a+b
        # return a