class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        taglist=['']*n
        for i in range(len(taglist)):
            taglist[i]="%s"%(i+1)
            if (i+1)%3==0 and (i+1)%5==0:
                taglist[i]="FizzBuzz"
            elif (i+1)%3==0:
                taglist[i]="Fizz"
            elif (i+1)%5==0:
                taglist[i]="Buzz"
        return taglist