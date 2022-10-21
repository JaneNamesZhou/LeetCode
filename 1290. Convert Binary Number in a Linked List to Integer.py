# Checked Date: 2022/10/20

# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
#
# Return the decimal value of the number in the linked list.
#
# The most significant bit is at the head of the linked list.
#
#
#
# Example 1:
#
#
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10


# Example 2:
#
# Input: head = [0]
# Output: 0
#
#
# Constraints:
#
# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.
 
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getDecimalValue(head: ListNode) -> int:
    result = 0
    node_i = head
    while node_i:
        result = result * 2 + node_i.val
        node_i = node_i.next
    return result


if __name__ == "__main__":
    e1 = ListNode(1)
    e2 = ListNode(0)
    e3 = ListNode(1)

    e1.next = e2
    e2.next = e3

    print(getDecimalValue(head=e1))
