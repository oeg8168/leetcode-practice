class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return self.solving(1, set(range(1, N + 1)))

    # Slow :(
    def solving(self, position, unusedNums):
        ans = 0
        if len(unusedNums) == 0:
            return 1

        for num in unusedNums:
            if num % position == 0 or position % num == 0:
                ans += self.solving(position + 1, set(unusedNums) - {num})
        return ans
