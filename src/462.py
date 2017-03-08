class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        median = sorted(nums)[len(nums) // 2]

        for num in nums:
            ans += abs(num - median)

        return ans
