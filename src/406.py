class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        newQueue = []

        for p in sorted(people, reverse=True, key=lambda x: (x[0], -x[1])):
            newQueue.insert(p[1], p)

        return newQueue
