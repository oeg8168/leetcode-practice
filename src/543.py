# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            depthL = dfs(node.left)
            depthR = dfs(node.right)
            self.ans = max(self.ans, depthL + depthR)
            return 1 + max(depthL, depthR)

        dfs(root)

        return self.ans
