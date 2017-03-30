class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for c in s:
            if c not in t:
                return False
            t = t[t.find(c) + 1:]

        return True
