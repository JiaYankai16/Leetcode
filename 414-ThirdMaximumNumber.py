class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1 or len(nums)==2:
            return max(nums)
        maxtag=max(nums)
        tag=maxtag
        for i in range(2):
            while tag in nums:
                nums.remove(tag)
            if len(nums)==0:
                return maxtag
            tag=max(nums)
        return max(nums)