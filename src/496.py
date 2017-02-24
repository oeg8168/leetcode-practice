class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        answers = []

        for num in findNums:
            ans = -1
            for target in nums[nums.index(num) + 1:]:
                if target > num:
                    ans = target
                    break

            answers.append(ans)

        return answers
