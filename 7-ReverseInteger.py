"""
@author:jiayankai
@date:2018/01/19
"""
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            tag=1
        else:
            tag=-1
        x=abs(x)
        num=0
        while(x>9):
            num=num*10+x%10
            x//=10
        num=(num*10+x)*tag
        if(num>(2**31-1) or num<(-1*(2**31))):
           return 0
        else:
           return num