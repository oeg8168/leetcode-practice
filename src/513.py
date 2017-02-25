# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.stack = []
        self.dfs(root, 1)

        value = 0
        maxDeaph = 0
        for element in self.stack:
            if element[1] > maxDeaph:
                value = element[0]
                maxDeaph = element[1]

        return value

    def dfs(self, node, depth):
        if node.left is not None:
            self.dfs(node.left, depth + 1)

        if node.right is not None:
            self.dfs(node.right, depth + 1)

        self.stack.append((node.val, depth))
