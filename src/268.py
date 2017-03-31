class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        if nums[0] != 0:
            return 0
        if nums[-1] != len(nums):
            return len(nums)

        for i, num in enumerate(nums):
            if i != num:
                return i

    def missingNumber_usingMath(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)
