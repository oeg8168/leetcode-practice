import itertools


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for c in itertools.combinations(range(10), num):
            hour = 0
            minute = 0
            for i in c:
                if i == 0:
                    hour += 8
                elif i == 1:
                    hour += 4
                elif i == 2:
                    hour += 2
                elif i == 3:
                    hour += 1
                elif i == 4:
                    minute += 32
                elif i == 5:
                    minute += 16
                elif i == 6:
                    minute += 8
                elif i == 7:
                    minute += 4
                elif i == 8:
                    minute += 2
                elif i == 9:
                    minute += 1

            if hour >= 12 or minute >= 60:
                continue

            if minute < 10:
                time = str(hour) + ':0' + str(minute)
            else:
                time = str(hour) + ':' + str(minute)

            ans.append(time)

        return ans
