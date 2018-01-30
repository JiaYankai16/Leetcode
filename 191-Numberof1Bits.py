class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        tag=0
        n=bin(n)[2:]
        for nn in n:
            if int(nn)==1:
                tag+=1
        return tag