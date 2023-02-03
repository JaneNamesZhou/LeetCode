# Checked Date: 2023/02/03

# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
#
#
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
#
# Input: head = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    if head == None:
        return None
    if head.next == None:
        return head
    result_head = ListNode(head.val)

    while head.next:
        result_head = ListNode(head.next.val,result_head)
        head = head.next
    return result_head


if __name__ == "__main__":
    e1 = ListNode(1)
    e2 = ListNode(2)
    e3 = ListNode(4)
    e4 = ListNode(1)
    e5 = ListNode(3)
    e6 = ListNode(4)

    e1.next = e2
    e2.next = e3


    print(reverseList(e1))
