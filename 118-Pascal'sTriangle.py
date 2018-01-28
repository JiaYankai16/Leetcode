class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        taglist=[[1],[1,1]]
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return taglist
        for i in range(2,numRows):
            newlist=[1]
            for j in range(1,len(taglist[i-1])):
                newlist.append(sum(taglist[i-1][j-1:j+1]))
            newlist.append(1)
            taglist.append(newlist)
        return taglist
            