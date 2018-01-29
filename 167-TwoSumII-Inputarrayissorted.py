class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        tagdict={}
        for i in range(len(numbers)):
            if target-numbers[i] in tagdict:
                return [tagdict[target-numbers[i]]+1,i+1]
            tagdict[numbers[i]]=i
                       