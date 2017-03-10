from math import sqrt


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        best = [area, 1]
        bestDiff = best[0] - best[1]

        for i in range(1, int(sqrt(area) + 1)):
            if area % i == 0:
                temp = [area // i, i]
                tempDiff = temp[0] - temp[1]

                if tempDiff < bestDiff:
                    best = temp

        return best
