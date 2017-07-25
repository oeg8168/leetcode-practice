class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in sorted(set(nums)):
            i = nums.index(num)
            if i % 2 == 1:
                return nums[i - 1]

        return nums[-1]

    # slow
