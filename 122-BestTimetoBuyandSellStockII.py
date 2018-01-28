class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        sumnum=0
        buynum=prices[0]
        for i in range(1,len(prices)):
            if prices[i]-buynum>0:
                sumnum+=prices[i]-buynum
            buynum=prices[i]
        return  sumnum
                