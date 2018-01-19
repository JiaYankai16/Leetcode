"""
@author:jiayankai
@date:2018/01/19
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxnum=[0]
        for i in range(len(s)):
            newdict={}
            num=0
            for j in range(i,len(s)):
                if s[j] in newdict:
                    break
                else:
                    newdict[s[j]]=True
                    num+=1
            maxnum.append(num)
        return max(maxnum)