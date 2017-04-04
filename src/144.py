# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if node:
            self.ans.append(node.val)
            self.dfs(node.left)
            self.dfs(node.right)
