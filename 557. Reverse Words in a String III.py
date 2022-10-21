# Date: 2022/10/20

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
        if s1[j] == ' ' or j == len(s1)-1:
            les = (j-i)//2
            for x in range(i,i+les):
                y = j-(x-i)-1
                s1[x], s1[y] = s1[y], s1[x]
            j = j+1
            i = j
        j = j+1
    return ''.join(s1)


if __name__ == "__main__":
    print(reverseWords(s="Let's take LeetCode contest"))
