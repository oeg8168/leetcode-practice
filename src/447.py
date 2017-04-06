class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for p1 in points:
            pointDist = {}

            for p2 in points:
                xDist = p1[0] - p2[0]
                yDist = p1[1] - p2[1]
                distance = xDist * xDist + yDist * yDist
                pointDist[distance] = 1 + pointDist.get(distance, 0)

            for dist in pointDist:
                ans += pointDist[dist] * (pointDist[dist] - 1)

        return ans
