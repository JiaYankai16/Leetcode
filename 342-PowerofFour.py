class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num>1:
            num=float(num)/4
        return num==1