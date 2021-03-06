class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        tag=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[tag]:
                tag+=1
                nums[tag]=nums[i]
        return tag+1
                