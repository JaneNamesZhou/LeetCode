# Checked Date: 2023/02/03

# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#
#
#
# Example 1:
#
# Input: nums = [3,2,3]
# Output: 3


# Example 2:
#
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?

from typing import List


def majorityElement(nums: List[int]) -> int:
    dict = {}
    result = nums[0]
    max = 1
    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = 1
        else:
            dict[nums[i]] += 1
        if dict[nums[i]] > max:
            result = nums[i]
            max = dict[nums[i]]
    return result


if __name__ == "__main__":
    print(majorityElement(nums=[6, 6, 6, 7, 7]))
