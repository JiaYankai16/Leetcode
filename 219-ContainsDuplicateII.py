class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        tagdict={}
        for i in range(len(nums)):
            if nums[i] in tagdict:
                if i-tagdict[nums[i]]<=k:
                    return True
            tagdict[nums[i]]=i
        return False
            