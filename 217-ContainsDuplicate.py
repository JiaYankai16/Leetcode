class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        tagdict={}
        for num in nums:
            if num in tagdict:
                return True
            else:
                tagdict[num]=True
        return False