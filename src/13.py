class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.upper()
        ans = 0
        romanTable = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        minusRomanTable = {'IV': -2, 'IX': -2, 'XL': -20,
                           'XC': -20, 'CD': -200, 'CM': -200}

        for key in romanTable.keys():
            ans += romanTable[key] * s.count(key)

        for key in minusRomanTable.keys():
            ans += minusRomanTable[key] * s.count(key)

        return ans
