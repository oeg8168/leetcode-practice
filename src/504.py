class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        elif num < 0:
            negative = True
            num = abs(num)
        else:
            negative = False

        ans = ''
        while num:
            ans = str(num % 7) + ans
            num = num // 7

        if negative:
            return '-' + ans
        else:
            return ans
