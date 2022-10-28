# Checked Date: 2022/10/28

# Given two binary strings a and b, return their sum as a binary string.
#
#
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"


# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

from typing import List


def addBinary(a: str, b: str) -> str:
    result = ''
    if len(a) > len(b):
        l = len(a)
    else:
        l = len(b)
    x = 0
    for i in range(l):
        if i < len(a):
            x = x + int(a[len(a) - 1 - i])
        if i < len(b):
            x = x + int(b[len(b) - 1 - i])
        if x > 1:
            result = str(x - 2) + result
            x = 1
        else:
            result = str(x) + result
            x = 0
    if x > 0:
        result = str(x) + result
    return result


if __name__ == "__main__":
    print(addBinary(a="11", b="1"))
