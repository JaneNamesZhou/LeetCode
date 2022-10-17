# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.


# Example 1:
#
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4


# Constraints:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    i = 0
    j = len(nums)-1
    if target <= nums[i]:
        return i
    if target == nums[j]:
        return j
    if target > nums[j]:
        return j+1
    while i+1 < j:
        mid = i + (j - i) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            i = mid
        if target < nums[mid]:
            j = mid
    return i+1


if __name__ == "__main__":
    print(searchInsert(nums = [1,3,5,6], target = 7))