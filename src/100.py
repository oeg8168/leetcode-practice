# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False

        return self.dfsCompare(p, q)

    def dfsCompare(self, p, q):
        if p.val != q.val:
            return False
        lFlag = True
        rFlag = True

        if (p.left is not None) and (q.left is not None):
            lFlag &= self.dfsCompare(p.left, q.left)
        elif (p.left is not None) != (q.left is not None):
            return False

        if (p.right is not None) and (q.right is not None):
            rFlag &= self.dfsCompare(p.right, q.right)
        elif (p.right is not None) != (q.right is not None):
            return False

        return lFlag & rFlag
