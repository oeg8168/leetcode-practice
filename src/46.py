from itertools import permutations


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for s in permutations(nums):
            ans.append(list(s))

        return ans
