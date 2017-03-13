class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nonZero = 0
        for idNum, num in enumerate(nums):
            if num != 0:
                nums.insert(nonZero, nums.pop(idNum))
                nonZero += 1
