class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        ''' # memory error
        if n <= 3:
            return True

        answer = [None, True, True, True]
        for i in range(4, n + 1):
            answer.append(not(answer[i - 1] and answer[i - 2] and answer[i - 3]))

        return answer[-1]
        '''

        return n % 4 != 0


print(Solution().canWinNim(4))
