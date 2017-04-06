from itertools import combinations


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        for comb in combinations(range(1, 10), k):
            if sum(comb) == n:
                ans.append(list(comb))

        return ans
