class Solution(object):
    def singleNumber_original(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []

        for num in nums:
            if num in temp:
                temp.remove(num)
            else:
                temp.append(num)

        return temp[0]

    # Ref:
    # https://discuss.leetcode.com/topic/42358/1-line-simple-python-solution
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums)) * 2 - sum(nums)  # Brilliant!!!
