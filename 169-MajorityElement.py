class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tagdict={}
        if len(nums)==1:
            return nums[0]
        for num in nums:
            if num in tagdict:
                tagdict[num]+=1
                if tagdict[num]>len(nums)/2:
                    return num
            else:
                tagdict[num]=1