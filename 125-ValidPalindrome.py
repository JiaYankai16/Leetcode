class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tagstr=''
        for ss in s:
            if ord(ss)<=ord('9') and ord(ss)>=ord('0'):
                tagstr+=ss
            if ord(ss)<=ord('Z') and ord(ss)>=ord('A'):
                tagstr+=chr(ord(ss)+32)
            if ord(ss)<=ord('z') and ord(ss)>=ord('a'):
                tagstr+=ss
        print(tagstr)
        return tagstr==tagstr[::-1]