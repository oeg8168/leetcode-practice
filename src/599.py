class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ans = list()
        minIndex = 0xFFFFFFFF
        for i, item in enumerate(list1):
            if item in list2:
                indexSum = i + list2.index(item)
                if indexSum <= minIndex:
                    ans.append(item)
                    minIndex = indexSum

        return ans
