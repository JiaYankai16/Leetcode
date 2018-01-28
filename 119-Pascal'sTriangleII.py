class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        taglist=[1,1]
        for i in range(2,rowIndex+1):
            newlist=[1]
            for j in range(1,len(taglist)+1):
                newlist.append(sum(taglist[j-1:j+1]))
            taglist=newlist
        return taglist