class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        taglist=[]
        for num in nums1:
            if num in nums2:
                if num not in taglist:
                    taglist.append(num)
        return taglist