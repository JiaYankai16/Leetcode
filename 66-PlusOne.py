class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        tag=1
        for i in range(1,len(digits)+1):
            digits[-i]+=tag
            tag=0
            if digits[-i]<=9:
                break
            digits[-i]%=10
            tag+=1
        if tag==1:
            digits.insert(0,1)
        return digits
            