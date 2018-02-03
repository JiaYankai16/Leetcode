class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        taglist=[n]
        while True:
            sum=0
            for i in str(n):
                sum += int(i) ** 2
            n = sum
            if n==1 or n in taglist:
                break
            taglist.append(n)
        return n == 1