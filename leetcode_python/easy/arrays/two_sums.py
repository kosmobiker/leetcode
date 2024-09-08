"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # brute-force solution
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i , j
        # elegant solution from leetcode
        d = {}
        for i in range(len(nums)):
            if target - nums[i] not in d:
                d[nums[i]] = i
            else:
                return [d[target - nums[i]], i]


if __name__ == "__main__":
    s = Solution()

    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    expected1 = [0, 1]
    r1 = s.twoSum(nums1, target1)
    assert r1 == expected1, f"Test Case 1 Failed: expected output {expected1}, but got {r1}"

    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    expected2 = [1, 2]
    r2 = s.twoSum(nums2, target2)
    assert r2 == expected2, f"Test Case 2 Failed: expected output {expected2}, but got {r2}"

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    expected3 = [0, 1]
    r3 = s.twoSum(nums3, target3)
    assert r3 == expected3, f"Test Case 3 Failed: expected output {expected3}, but got {r3}"

    # Test case 4
    nums4 = [3, 2, 3]
    target4 = 6
    expected4 = [0, 2]
    r4 = s.twoSum(nums4, target4)
    assert r4 == expected4, f"Test Case 4 Failed: expected output {expected4}, but got {r4}"
