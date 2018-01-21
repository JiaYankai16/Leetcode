class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        tag=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[tag]=nums[i]
                tag+=1
        return tag