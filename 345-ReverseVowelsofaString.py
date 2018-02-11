class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        taglist=[]
        for ss in s:
            if ss in ['a','e','i','o','u','A','E','I','O','U']:
                taglist.append(ss)
        j=-1
        strstr=''
        for ss in s:
            if ss in ['a','e','i','o','u','A','E','I','O','U']:
                strstr+=taglist[j]
                j-=1
            else:
                strstr+=ss
        return strstr