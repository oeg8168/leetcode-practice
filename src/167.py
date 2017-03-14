class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        checked = []
        for num in filter(lambda x: x <= target, numbers):
            if num in checked:
                continue
            else:
                checked.append(num)

                complement = target - num
                if complement in numbers:
                    index1 = numbers.index(num) + 1
                    index2 = len(numbers) - numbers[::-1].index(complement)

                    return index1, index2
