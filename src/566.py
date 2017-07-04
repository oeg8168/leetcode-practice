class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums:
            return nums

        flatten = [item for oneRow in nums for item in oneRow]

        if len(flatten) != (r * c):
            return nums

        if r == 1:
            return [flatten]

        ans = list()
        for row in range(r):
            ans.append([flatten[row * c + col] for col in range(c)])

        return ans

# so ugly :(
