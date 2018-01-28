class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buynum=prices[0]
        maxpro=0
        for i in range(1,len(prices)):
            if prices[i]<buynum:
                buynum=prices[i]
            if prices[i]-buynum>maxpro:
                maxpro=prices[i]-buynum
        return maxpro