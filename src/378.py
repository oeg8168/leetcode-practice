class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        allElement = []
        for row in matrix:
            allElement += row

        return sorted(allElement)[k - 1]
