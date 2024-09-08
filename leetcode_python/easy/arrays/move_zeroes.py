"""
Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums) and j < len(nums):
            if nums[i] != 0:
                i += 1
                j += 1
            elif nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                j += 1


if __name__ == "__main__":
    s = Solution()

    # Test case 1
    nums1 = [0, 1, 0, 3, 12]
    expected1 = [1, 3, 12, 0, 0]
    s.moveZeroes(nums1)
    assert nums1 == expected1, f"Test Case 1 Failed: expected output {expected1}, but got {nums1}"

    # Test case 2
    nums2 = [0]
    expected2 = [0]
    s.moveZeroes(nums2)
    assert nums2 == expected2, f"Test Case 1 Failed: expected output {expected2}, but got {nums2}"

    # Test case 3
    nums3 = [0, 0, 1]
    expected2 = [1, 0, 0]
    s.moveZeroes(nums3)
    assert nums3 == expected2, f"Test Case 3 Failed: expected output {expected2}, but got {nums3}"
