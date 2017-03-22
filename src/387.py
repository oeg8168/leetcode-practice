class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counted = []
        for c in s:
            if c not in counted:
                counted.append(c)
                if s.count(c) == 1:
                    return s.index(c)

        return -1
