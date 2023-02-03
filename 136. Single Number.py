# Checked Date: 2023/02/03

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
#
#
# Example 1:
#
# Input: nums = [2,2,1]
# Output: 1


# Example 2:
#
# Input: nums = [4,1,2,1,2]
# Output: 4


# Example 3:
#
# Input: nums = [1]
# Output: 1
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# Each element in the array appears twice except for one element which appears only once.

from typing import List


def isingleNumber(  nums: List[int]) -> int:
    dict = {}
    result = nums[0]
    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = 1
        else:
            dict[nums[i]] += 1
        if dict[nums[i]] > 1:
            del dict[nums[i]]
    for item in dict.items():
        result = item[0]
    return result


if __name__ == "__main__":
    print(isingleNumber(nums = [4,1,2,1,2]))
