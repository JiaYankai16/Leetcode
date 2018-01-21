class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return str(1)
        strstr=self.countAndSay(n-1)
        newstr=''
        tag=0
        for i in range(1,len(strstr)):
            if strstr[i]!=strstr[tag]:
                newstr+=str(i-tag)+strstr[tag]
                tag=i
        newstr+=str(len(strstr)-tag)+strstr[-1]
        return newstr