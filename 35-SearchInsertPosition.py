class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        for i in range(len(nums)):
            if nums[i]>=target:
                break
        if i==len(nums)-1 and nums[i]<target:
            return i+1
        return i