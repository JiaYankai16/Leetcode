class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        firsttag=1
        lasttag=2
        for i in range(2,n):
            firsttag,lasttag=lasttag,firsttag+lasttag
        return lasttag