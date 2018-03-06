class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        tag=str(bin(num)[2:])
        tagstr=''
        for i in tag:
            if i=='1':
                tagstr+='0'
            else:
                tagstr+='1'
        return int(tagstr,2)
        