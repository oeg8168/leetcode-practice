class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        charList = list(s)
        charFreq = [c * charList.count(c) for c in set(charList)]
        ans = sorted(charFreq, key=len, reverse=True)

        return ''.join(ans)
