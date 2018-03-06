class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        tagdict = {}
        for i in range(1, int(pow(area, 0.5)) + 1):
            if int(area / i) == area/i:
                tagdict[area / i - i] = [int(area / i), i]
        minnum=min(tagdict)
        return tagdict[minnum]