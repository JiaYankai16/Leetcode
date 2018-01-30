class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        tag=bin(n)[2:]
        tag=(32-len(tag))*'0'+tag
        return int(tag[::-1],2)