class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        tagdict={}
        for ss in s:
            if ss in tagdict:
                tagdict[ss]+=1
            else:
                tagdict[ss]=1
        print(tagdict)
        for ss in s:
            if tagdict[ss]==1:
                return list(s).index(ss)
        return -1