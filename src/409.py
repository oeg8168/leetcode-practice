from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        hasOdd = 0
        for i in Counter(s).values():
            if i % 2 == 1:
                hasOdd = 1
                ans += (i - 1)
            else:
                ans += i

        return ans + hasOdd
