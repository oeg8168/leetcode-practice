class Solution(object):
    def findDisappearedNumbers_OriginalTLE(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = [x + 1 for x in range(len(nums))]

        for i in set(nums):
            if i in missing:
                missing.remove(i)

        return missing

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = [x + 1 for x in range(len(nums))]
        return list(set(missing) ^ set(nums))
