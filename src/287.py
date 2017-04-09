class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bucket = set()
        for num in nums:
            if num in bucket:
                return num
            else:
                bucket.add(num)
