class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1]
        for i in range(min(n, 10)):
            if len(ans) < 3:
                ans += [ans[-1] * 9]
            else:
                ans += [ans[-1] * (9 - i + 1)]
        return sum(ans)

    def countNumbersWithUniqueDigits_lookUpTable(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [1, 9, 81, 648, 4536, 27216, 136080,
                 544320, 1632960, 3265920, 3265920]
        return sum(table[:min(n + 1, 10)])
