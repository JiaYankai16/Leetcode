class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        tagstr=''
        while n>0:
            if n%26==0:
                tagstr='Z'+tagstr
                n-=26
            else:
                tagstr=chr(ord('A')+n%26-1)+tagstr
                n-=n%26
            n//=26
        return tagstr
        