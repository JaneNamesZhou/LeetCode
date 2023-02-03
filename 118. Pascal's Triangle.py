# Checked Date: 2023/01/31

# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#
#
#
# Example 1:
#
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


# Example 2:
#
# Input: numRows = 1
# Output: [[1]]
#
#
# Constraints:
#
# 1 <= numRows <= 30

from typing import List


def generate(numRows) -> List[List[int]]:
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1],[1,1]]
    else:
        x = generate(numRows - 1)
        y =x[-1]
        z =[1]
        for i in range(len(y)-1):
            z.append(y[i]+y[i+1])
        z.append(1)
        x.append(z)
        return x


if __name__ == "__main__":
    print(generate(5))
