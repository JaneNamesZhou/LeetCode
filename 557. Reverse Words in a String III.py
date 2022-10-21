# Checked Date: 2022/10/20

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
#
#
# Example 1:
#
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"


# Example 2:
#
# Input: s = "God Ding"
# Output: "doG gniD"
#
#
# Constraints:
#
# 1 <= s.length <= 5 * 10^4
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.

from typing import List


def reverseWords(s: str) -> str:
    s1 = list(s)
    i = 0
    j = 0
    while j < len(s1):
        if j == len(s1) - 1 or s1[j + 1] == ' ':
            les = (j - i) // 2 + 1
            for x in range(0, les):
                s1[i + x], s1[j - x] = s1[j - x], s1[i + x]
            j = j + 2
            i = j
            continue
        j = j + 1
    return ''.join(s1)


if __name__ == "__main__":
    print(reverseWords(s="a b d ee$#% aef$ea eaef eaj ae##ea'fe"))
