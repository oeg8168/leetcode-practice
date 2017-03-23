class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        ans = 0
        for c in s.upper():
            ans = ans * 26 + (alphabet.index(c) + 1)

        return ans

    # faster (using unicode value)
    def titleToNumber_anotherSolution(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for c in s.upper():
            ans = ans * 26 + ord(c) - 64

        return ans
