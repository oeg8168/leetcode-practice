class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanTable = {1: 'I', 5: 'V', 10: 'X',
                      50: 'L', 100: 'C', 500: 'D', 1000: 'M',
                      4: 'IV', 9: 'IX', 40: 'XL',
                      90: 'XC', 400: 'CD', 900: 'CM'}

        ans = ''
        for i in sorted(romanTable.keys(), reverse=True):
            ans = ans + romanTable[i] * (num // i)
            num = num % i

        return ans
