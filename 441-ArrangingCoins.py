class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        tag=1
        while n>0:
            n-=tag
            tag+=1
        if n==0:
            return tag-1
        else:
            return tag-2