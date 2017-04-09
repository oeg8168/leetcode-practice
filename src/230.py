# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.sortedElement = []
        self.inorder(root)
        return self.sortedElement[k - 1]

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.sortedElement.append(node.val)
            self.inorder(node.right)

    def kthSmallest_earlyTermination(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.n = 0
        self.k = k
        self.sortedElement = []
        self.inorder_earlyTermination(root)

        return self.sortedElement[k - 1]

    def inorder_earlyTermination(self, node):
        if self.n >= self.k:
            return
        if node:
            self.inorder_earlyTermination(node.left)
            self.sortedElement.append(node.val)
            self.n += 1
            self.inorder_earlyTermination(node.right)
