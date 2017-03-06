class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        answer = 0

        for idT, t in enumerate(timeSeries):
            if idT == 0:
                start = t
            else:
                start = max(timeSeries[idT - 1] + duration, timeSeries[idT])
            end = timeSeries[idT] + duration

            answer += end - start

        return answer

    # Another solution : All time - overlaping
    # Ref: https://discuss.leetcode.com/topic/77360/python-solution-for-teemo
    def findPoisonedDuration_forumSolution(self, timeSeries, duration):
        ans = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            ans -= max(0, duration - (timeSeries[i] - timeSeries[i - 1]))
        return ans
