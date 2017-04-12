class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        self.palidomeDP = [[-1 for i in range(len(s))] for i in range(len(s))]
        return self.getLPS(0, len(s) - 1)

    def getLPS(self, i, j):
        if self.palidomeDP[i][j] == -1:
            if i > j:
                return 0
            elif i == j:    # single character
                return 1
            elif self.s[i] == self.s[j]:    # same character
                self.palidomeDP[i][j] = self.getLPS(i + 1, j - 1) + 2
            else:
                cutLeft = self.getLPS(i + 1, j)
                cutRight = self.getLPS(i, j - 1)
                self.palidomeDP[i][j] = max(cutLeft, cutRight)

        return self.palidomeDP[i][j]

    '''
    My solution above (TLE)
    The logic is correct but not efficient enough
    So here are some forum solutions provided by other users
    '''

    # Ref:
    # https://discuss.leetcode.com/topic/79011/fast-and-concise-python-solution-that-actually-gets-ac
    def longestPalindromeSubseq_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}

        def f(s):
            if s not in d:
                maxL = 0
                for c in set(s):
                    i, j = s.find(c), s.rfind(c)
                    maxL = max(maxL, 1 if i == j else 2 + f(s[i + 1:j]))
                d[s] = maxL
            return d[s]
        return f(s)

    # Ref:
    # https://discuss.leetcode.com/topic/78625/python-dp-o-n-space-o-n-2-time
    def longestPalindromeSubseq_2_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[1] * 2 for _ in range(n)]
        for j in range(1, len(s)):
            for i in reversed(range(0, j)):
                if s[i] == s[j]:
                    dp[i][j % 2] = 2 + \
                        dp[i + 1][(j - 1) % 2] if i + 1 <= j - 1 else 2
                else:
                    dp[i][j % 2] = max(dp[i + 1][j % 2], dp[i][(j - 1) % 2])
        return dp[0][(n - 1) % 2]

    def longestPalindromeSubseq_2_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [1] * n
        for j in range(1, len(s)):
            pre = dp[j]
            for i in reversed(range(0, j)):
                tmp = dp[i]
                if s[i] == s[j]:
                    dp[i] = 2 + pre if i + 1 <= j - 1 else 2
                else:
                    dp[i] = max(dp[i + 1], dp[i])
                pre = tmp
        return dp[0]
