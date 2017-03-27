class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timeMinutes = []
        for t in timePoints:
            hour = int(t[:2])
            minute = int(t[3:])
            timeMinutes.append(hour * 60 + minute)

        timeMinutes = sorted(timeMinutes)

        headDiff = timeMinutes[-1] - timeMinutes[0]
        ans = min(headDiff, 1440 - headDiff)
        for i, t in enumerate(timeMinutes[1:]):
            timeDiff = t - timeMinutes[i]
            ans = min(ans, min(timeDiff, 1440 - timeDiff))
