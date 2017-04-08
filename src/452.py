# Ref: https://discuss.leetcode.com/topic/66772/greedy-python-132-ms
# Brilliant solution!


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        shoot = float('inf')

        for x0, x1 in sorted(points, reverse=True):
            if x1 < shoot:
                ans += 1
                shoot = x0

        return ans
