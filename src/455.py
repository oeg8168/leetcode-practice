class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(g) == 0 or len(s) == 0:
            return 0

        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)

        assigned = 0
        for child in g:
            if s[0] >= child:
                s.pop(0)
                assigned += 1
                if len(s) == 0:
                    break

        return assigned
