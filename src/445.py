# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        input1 = 0
        curr = l1
        while curr:
            input1 = input1 * 10 + curr.val
            curr = curr.next

        input2 = 0
        curr = l2
        while curr:
            input2 = input2 * 10 + curr.val
            curr = curr.next

        result = input1 + input2
        if result == 0:
            return ListNode(0)

        ans = None
        while result:
            digit = result % 10
            temp = ListNode(digit)
            temp.next = ans
            ans = temp
            result = result // 10

        return ans
