# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prevNode = None
        currNode = head

        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

        return prevNode

    # Ref:
    # https://discuss.leetcode.com/topic/14043/python-iterative-and-recursive-solution
    def reverseList_recursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def helper(node, prev=None):
            if not node:
                return prev
            nextNode = node.next
            node.next = prev
            return helper(nextNode, node)

        return helper(head)
