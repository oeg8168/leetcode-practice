class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0

        answer = 0
        longestSlice = [A[0], A[1]]
        sliceInterval = longestSlice[1] - longestSlice[0]

        for num in A[2:]:
            interval = num - longestSlice[-1]

            if interval != sliceInterval:
                answer += self.findSubSlices(longestSlice)
                longestSlice = [longestSlice[-1], num]
                sliceInterval = longestSlice[1] - longestSlice[0]
            else:
                longestSlice.append(num)

        answer += self.findSubSlices(longestSlice)

        return answer

    def findSubSlices(self, A):
        if len(A) < 3:
            return 0

        n = len(A) - 2
        slices = (n + 1) * n / 2

        return int(slices)

    def numberOfArithmeticSlices_anotherSolution(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        answer = 0
        current = 0

        for i in range(2, len(A)):
            if (A[i] - A[i - 1]) == (A[i - 1] - A[i - 2]):
                current += 1
                answer += current
            else:
                current = 0

        return answer
