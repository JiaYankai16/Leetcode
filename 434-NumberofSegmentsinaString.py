class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        taglist=s.split(' ')
        while '' in taglist:
            taglist.remove('')
        return len(taglist)