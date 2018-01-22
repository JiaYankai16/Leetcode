class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        taglist=s.split(' ')
        for i in range(1,len(taglist)+1):
            if len(taglist[-i])!=0:
                return len(taglist[-i])
        return 0