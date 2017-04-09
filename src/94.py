# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        self.ans = []
        self.dfsInorder(root)
        return self.ans

    def dfsInorder(self, node):
        if node.left is not None:
            self.dfsInorder(node.left)

        self.ans.append(node.val)

        if node.right is not None:
            self.dfsInorder(node.right)

    # Same logic but different style
    # Ref:
    # https://discuss.leetcode.com/topic/21350/python-recursive-and-iterative-solutions
    def inorderTraversal_anotherSolution(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        self.dfsInorder_anotherSolution(root)
        return self.ans

    def dfsInorder_anotherSolution(self, node):
        if node:
            self.dfsInorder_anotherSolution(node.left)
            self.ans.append(node.val)
            self.dfsInorder_anotherSolution(node.right)
