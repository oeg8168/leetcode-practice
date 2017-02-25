class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        ones = 0
        for num in nums:
            if num == 0:
                answer = max(answer, ones)
                ones = 0
            else:
                ones += 1

        answer = max(answer, ones)

        return answer
