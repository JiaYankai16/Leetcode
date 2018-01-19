"""
@author:jiayankai
@date:2018/01/19
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_dict={}
        for i in range(len(nums)):
            if (target-nums[i]) in new_dict:
                return [new_dict[target-nums[i]],i]
            else:
                new_dict[nums[i]]=i