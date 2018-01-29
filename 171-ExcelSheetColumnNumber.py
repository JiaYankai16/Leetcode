class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num=0
        for ss in s:
            num=num*26+ord(ss)-ord('A')+1
        return num