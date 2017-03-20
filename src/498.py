class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        totalDiagonal = len(matrix) + len(matrix[0]) - 1
        diagonalLines = [[] for d in range(totalDiagonal)]

        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                diagonalLines[i + j].append(item)

        ans = []
        flip = True
        for diagonal in diagonalLines:
            if flip:
                ans += diagonal[::-1]
            else:
                ans += diagonal[::1]

            flip = not flip

        return ans
