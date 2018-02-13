class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tlist=list(t)
        for ss in s:
            if ss in tlist:
                tlist.remove(ss)
            else:
                return ss
        return tlist[0]