# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        self.allNode = []
        self.deepest = 0
        self.dfs(root, 0)

        answer = [None for i in range(self.deepest + 1)]

        for node in self.allNode:
            if answer[node[0]] is None:
                answer[node[0]] = node[1]
            elif answer[node[0]] < node[1]:
                answer[node[0]] = node[1]

        return answer

    def dfs(self, root, depth):
        if root.left is not None:
            self.dfs(root.left, depth + 1)
        if root.right is not None:
            self.dfs(root.right, depth + 1)

        self.allNode.append((depth, root.val))
        self.deepest = max(self.deepest, depth)

    # Could be better if using BFS
