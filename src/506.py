class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sortedNums = sorted(nums, reverse=True)

        ans = [str(sortedNums.index(num) + 1) for num in nums]
        if len(ans) > 0:
            ans[ans.index('1')] = "Gold Medal"
        if len(ans) > 1:
            ans[ans.index('2')] = "Silver Medal"
        if len(ans) > 2:
            ans[ans.index('3')] = "Bronze Medal"

        return ans
