"""
@author:jiayankai
@date:2018/01/19
"""
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)==str(x)[::-1]