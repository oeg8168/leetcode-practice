# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []

        ans = list()
        queue = [root]
        while len(queue) != 0:
            levelItems = [item.val for item in queue]
            ans.append(float(sum(levelItems)) / len(levelItems))

            tempQueue = list()
            for item in queue:
                if item.left:
                    tempQueue.append(item.left)
                if item.right:
                    tempQueue.append(item.right)
            queue = tempQueue

        return ans
