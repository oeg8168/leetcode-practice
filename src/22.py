class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.n = n
        self.ans = []
        self.dfs('(', 1, 0)

        return self.ans

    def dfs(self, currentString, leftCount, rightCount):
        if rightCount > leftCount:
            return
        if leftCount > self.n or rightCount > self.n:
            return

        if (leftCount + rightCount) == (2 * self.n):
            self.ans.append(currentString)
        else:
            self.dfs(currentString + '(', leftCount + 1, rightCount)
            self.dfs(currentString + ')', leftCount, rightCount + 1)
