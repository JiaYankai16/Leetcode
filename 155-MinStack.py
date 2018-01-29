class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.taglist=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.taglist.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        self.taglist.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.taglist[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.taglist)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()