# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 1)

    def dfs(self, node, depth):
        leftDepth = 0
        rightDepth = 0
        if node.left is not None:
            leftDepth = self.dfs(node.left, depth + 1)
        if node.right is not None:
            rightDepth = self.dfs(node.right, depth + 1)

        return max(depth, leftDepth, rightDepth)
