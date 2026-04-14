class Solution(object):
    def climbStairs(self, n):
        if n==1:
            return 1
        if n==2:
            return 2
        lst_check=[0]*(n+1)
        lst_check[1]=1
        lst_check[2]=2

        for i in range(3,n+1):
            lst_check[i]=lst_check[i-1]+lst_check[i-2]
        return lst_check[n]
        