# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.allNode = []
        self.dfs(root)
        self.allNode = sorted(self.allNode)

        minDiff = self.allNode[1] - self.allNode[0]
        for i, val in enumerate(self.allNode[1:]):
            tempDiff = val - self.allNode[i]
            if tempDiff < minDiff:
                minDiff = tempDiff

        return minDiff

    def dfs(self, node):
        if node.left is not None:
            self.dfs(node.left)
        if node.right is not None:
            self.dfs(node.right)

        self.allNode.append(node.val)
