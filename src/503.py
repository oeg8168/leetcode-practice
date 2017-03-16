class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [-1] * len(nums)
        stack = [(i, num) for i, num in enumerate(nums)]
        stack = stack[::-1]

        for i, num in enumerate(nums):
            while stack != [] and stack[0][1] < num:
                pair = stack.pop(0)
                ans[pair[0]] = num

            stack.insert(0, (i, num))
        return ans

    # A little faster
    def nextGreaterElements_anotherSolution(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        originLength = len(nums)
        ans = [-1] * len(nums)

        nums = nums * 2
        stack = []

        for i, num in enumerate(nums):
            while stack != [] and stack[0][1] < num:
                pair = stack.pop(0)
                ans[pair[0]] = num

            stack.insert(0, (i % originLength, num))

        return ans
