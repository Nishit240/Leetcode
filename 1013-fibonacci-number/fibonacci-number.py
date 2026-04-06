class Solution:

    # def func(self, num: int) -> int:
    #     if num == 0 or num == 1:
    #         return num
    #     return self.func(num-1) + self.func(num-2)

    def fib(self, n: int) -> int:

        # answer = self.func(n)
        # return(answer)
        
        a,b=0,1
        for i in range(n):
            a,b=b,a+b
        return a