# Checked Date: 2023/01/30

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true


# Example 2:
#
# Input: s = "()[]{}"
# Output: true


# Example 3:
#
# Input: s = "(]"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.

from typing import List


def isValid(s: str) -> bool:
    if (len(s)) % 2 == 1:
        return False
    x = []
    for i in range(len(s)):
        if s[i] == '(':
            x.append(1)
            continue
        if s[i] == ')':
            if (len(x) > 0 and x[len(x) - 1] - 1 != 0) or len(x) == 0:
                return False
            if len(x) > 0:
                del x[len(x) - 1]
            continue

        if s[i] == '[':
            x.append(2)
            continue

        if s[i] == ']':
            if (len(x) > 0 and x[len(x) - 1] - 2 != 0) or len(x) == 0:
                return False
            if len(x) > 0:
                del x[len(x) - 1]
            continue
        if s[i] == '{':
            x.append(3)
            continue

        if s[i] == '}':
            if (len(x) > 0 and x[len(x) - 1] - 3 != 0) or len(x) == 0:
                return False
            if len(x) > 0:
                del x[len(x) - 1]
            continue
    if len(x) == 0:
        return True
    return False


if __name__ == "__main__":
    print(isValid(s="()"))
