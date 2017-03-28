class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return True if len(nums) != len(set(nums)) else False

    # Ref: https://discuss.leetcode.com/topic/28522/one-line-solution-in-python
    def containsDuplicate_simpler(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
