class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        fast=0
        for num in nums:
            if num!=0:
                nums[fast]=num
                fast+=1
        nums[fast:]=[0]*(len(nums)-fast)