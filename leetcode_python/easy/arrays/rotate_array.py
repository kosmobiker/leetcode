"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) #to fix an issue when number of rotations is higher than length of array
        res = nums[-k:] + nums[:-k]
        nums[:] = res


if __name__ == '__main__':
    s = Solution()
    # Test case 1
    nums1 = [1,2,3,4,5,6,7]
    expected_output1 = [5,6,7,1,2,3,4]
    k = 3
    s.rotate(nums1, k)
    assert nums1 == expected_output1, f"Test Case 1 Failed: expected output {expected_output1}, but got {nums1}"

    # Test case 2
    nums2 = [1, 2, 3, 4, 5]
    expected_output2 = [1, 2, 3, 4, 5]
    k = 0
    s.rotate(nums2, k)
    assert nums2 == expected_output2, f"Test Case 1 Failed: expected output {expected_output2}, but got {nums2}"

    # Test case 3
    nums3 = [-1,-100,3,99]
    expected_output3 = [3,99,-1,-100]
    k = 2
    s.rotate(nums3, k)
    assert nums2 == expected_output2, f"Test Case 1 Failed: expected output {expected_output2}, but got {nums2}"
    
