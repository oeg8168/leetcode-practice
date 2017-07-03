# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if (not t1) and (not t2):
            return None
        elif not t1:
            ans = TreeNode(t2.val)
        elif not t2:
            ans = TreeNode(t1.val)
        else:
            ans = TreeNode(t1.val + t2.val)

        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)

        return ans
