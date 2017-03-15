class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        minimal = min(nums)
        for num in nums:
            ans += num - minimal
        return ans

    # Brilliant!
    # Ref: https://discuss.leetcode.com/topic/66562/simple-one-liners
    def minMoves_anotherSolution(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)
