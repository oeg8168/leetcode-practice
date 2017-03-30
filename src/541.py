# this code is dirty...

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        pieces = len(s) // (2 * k)
        for i in range(pieces):
            start = i * k * 2
            end = start + k
            s = s[:start] + s[start:end][::-1] + s[end:]
        if (len(s) % (k * 2)) < k:
            return s[:pieces * k * 2] + s[pieces * k * 2:][::-1]
        else:
            return s[:pieces * k * 2] + s[pieces * k * 2:pieces * k * 2 + k][::-1] + s[pieces * k * 2 + k:]
