class Solution:
    def longestPalindrome(self, s):
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
        sumtag=0
        flag=0
        for tag in tagdict:
            if tagdict[tag]%2==0:
                sumtag+=tagdict[tag]
            else:
                flag=1
                sumtag+=tagdict[tag]-1
        return sumtag+flag