class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tag=0
        maxnum=0
        for num in nums:
            if num!=1:
                tag=0
            else:
                tag+=1
                maxnum=max(tag,maxnum)
        return maxnum