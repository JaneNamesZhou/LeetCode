# Checked Date: 2022/10/20

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
#
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


# Example 2:
#
# Input: nums = [0]
# Output: [0]
#
#
# Constraints:
#
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1

from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 0  # the num of zeroes
    while i < len(nums):
        if nums[i] != 0:
            nums[i], nums[i - j] = nums[i - j], nums[i]
        else:
            j = j + 1
        i = i + 1
    return nums


if __name__ == "__main__":
    print(moveZeroes(nums=[0, 1, 0, 3, 12]))
