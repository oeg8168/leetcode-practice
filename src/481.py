class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        S = '122'
        digit, anotherDigit = '1', '2'
        for i in range(2, n):
            S = S + digit * int(S[i])
            if len(S) > n:
                break
            digit, anotherDigit = anotherDigit, digit

        return S[:n].count('1')
