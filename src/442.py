class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        prev = 0
        for num in sorted(nums):
            if num == prev:
                ans.append(num)
            prev = num

        return ans

    # Without sorting
    def findDuplicates_anotherSolution(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Using the input array itself as a hash
        # to store which numbers have been seen before.
        # Ref:
        # https://discuss.leetcode.com/topic/64979/python-o-n-time-o-1-space
        res = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return res
