# Checked Date: 2023/01/30

# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"


# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# Follow up: Could you solve it without converting the integer to a string?

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if range(len(strs)) == 1:
        return ""
    str = strs[0]
    for i in range(len(strs) - 1):
        s = ""
        length = len(str) if (len(str) < len(strs[i + 1])) else len(strs[i + 1])
        for j in range(length):
            if strs[i][j] == strs[i + 1][j]:
                s = s + strs[i + 1][j]
            else:
                str = s
                break
        str = s
    return str


if __name__ == "__main__":
    print(longestCommonPrefix(strs=["flower", "flow", "flight"]))
