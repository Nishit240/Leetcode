class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # mp = 0
        # for i in range (len(prices)):
        #     for j in range (i+1, len(prices)):
        #         if prices[j] > prices[i]:
        #             p = prices[j] - prices[i]
        #             mp = max(mp,p)
        # return mp

        # mp = 0
        # minp = 10**5
        # for i in range(len(prices)):
        #     minp = min(minp, prices[i])
        #     mp = max(mp,prices[i] - minp)
        # return mp

        s = float('inf')
        p = 0
        for i in prices:
            if i < s:
                s = i
            elif i - s > p:
                p = i - s
        return p















         
        

        