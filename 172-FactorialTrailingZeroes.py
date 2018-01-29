class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num=0
        while n>=5:
            n//=5
            num+=n
        return num