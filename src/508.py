# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        self.subtreeSums = []
        self.dfs(root)

        maxFreq = 0
        summary = {key: 0 for key in set(self.subtreeSums)}
        for subtreeSum in self.subtreeSums:
            summary[subtreeSum] += 1
            maxFreq = max(summary[subtreeSum], maxFreq)

        return [x for x in summary.keys() if summary[x] is maxFreq]

    def dfs(self, root):
        subtreeSum = root.val

        if root.left is not None:
            subtreeSum += self.dfs(root.left)
        if root.right is not None:
            subtreeSum += self.dfs(root.right)

        self.subtreeSums.append(subtreeSum)

        return subtreeSum
