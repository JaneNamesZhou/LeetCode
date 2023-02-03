# Checked Date: 2023/02/03

# Given the head of a singly linked list, return true if it is a
# palindrome
#  or false otherwise.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
#
#
# Follow up: Could you do it in O(n) time and O(1) space?

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    list = []
    while head:
        list.append(head.val)
        head = head.next
    length = len(list)
    for i in range(length):
        if list[i] != list[length - 1 - i]:
            return False
    return True


if __name__ == "__main__":
    e1 = ListNode(1)
    e2 = ListNode(2)
    e3 = ListNode(3)
    e4 = ListNode(1)

    e1.next = e2
    e2.next = e3
    e3.next = e4

    print(isPalindrome(e1))
