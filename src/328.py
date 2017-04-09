# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None) or (head.next is None):
            return head

        odd = head
        evenHead = head.next
        even = evenHead

        while (even is not None) and (even.next is not None):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead

        return head

    # Ref: https://discuss.leetcode.com/topic/34309/clear-python-solution
    def oddEvenList_anotherSolution(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddHead = ListNode(0)
        odd = oddHead
        evenHead = ListNode(0)
        even = evenHead

        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None

        odd.next = evenHead.next

        return oddHead.next
