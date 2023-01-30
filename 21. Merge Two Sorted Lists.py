# Checked Date: 2023/01/30

# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#
#
# Example 1:
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]


# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []


# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
#
# Constraints:
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    if list1 == None and list2 == None:
        return None
    if list1 == None:
        return list2
    if list2 == None:
        return list1
    if list1.val < list2.val:
        result = ListNode(list1.val)
        list1 = list1.next
        if list1 == None:
            result.next = list2
            return result
    else:
        result = ListNode(list2.val)
        list2 = list2.next
        if list2 == None:
            result.next = list1
            return result

    x = result
    while list1:
        while list2:
            if list1 == None:
                x.next = list2
                return result
            if list1.val < list2.val:
                x.next = list1
                x = x.next
                list1 = list1.next
            else:
                x.next = list2
                x = x.next
                list2 = list2.next
        if list2 == None:
            x.next = list1
            return result

    return result


if __name__ == "__main__":
    e1 = ListNode(1)
    e2 = ListNode(2)
    e3 = ListNode(4)
    e4 = ListNode(1)
    e5 = ListNode(3)
    e6 = ListNode(4)

    e1.next = e2
    e2.next = e3
    e4.next = e5
    e5.next = e6

    print(mergeTwoLists(e6, e6))
