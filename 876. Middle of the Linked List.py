# Checked Date: 2022/10/20

# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.
#
#
#
# Example 1:
#
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.


# Example 2:
#
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: ListNode):
    result = head
    node_i = head
    i = 0
    while node_i:
        i = i + 1
        if i % 2 ==0:
            result = result.next
        node_i = node_i.next
    return result


if __name__ == "__main__":
    e1 = ListNode(1)
    e2 = ListNode(2)
    e3 = ListNode(3)
    e4 = ListNode(4)
    e5 = ListNode(5)
    e6 = ListNode(6)

    e1.next = e2
    e2.next = e3
    e3.next = e4
    e4.next = e5
    e5.next = e6

    print(middleNode(head=e1))
