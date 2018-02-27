class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        tag=0
        for gg in g:
            for ss in s:
                if gg<=ss:
                    tag+=1
                    s.remove(ss)
                    break
        return tag