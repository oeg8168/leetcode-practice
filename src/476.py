class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        for i in range(num.bit_length()):
            num = num ^ 2**i

        return num
