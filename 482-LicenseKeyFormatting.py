class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        tag=0
        tagstr=''
        for i in range(1,len(S)+1):
            if tag==K:
                tagstr='-'+tagstr
                tag=0
            if S[-i]!='-':
                if ord(S[-i])<=ord('z') and ord(S[-i])>=ord('a'):
                    tagstr=chr(ord(S[-i])-32)+tagstr
                else:
                    tagstr=S[-i]+tagstr
                tag+=1
        if tag==0:
            return tagstr[1:]
        else:
            return tagstr