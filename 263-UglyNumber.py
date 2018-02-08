class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0:
            return False
        while True:
            if num%2==0:
                num//=2
                continue
            if num%5==0:
                num//=5
                continue
            if num%3==0:
                num//=3
                continue
            break
        if num==1:
            return True
        return False