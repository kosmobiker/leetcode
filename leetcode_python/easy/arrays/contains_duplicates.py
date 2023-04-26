"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        t = set(nums)
        return False if len(t) == len(nums) else True
    
    
if __name__ == '__main__':
    s = Solution()
    # Test case 1
    nums1 = [1,2,3,1]
    expected1 = True
    result1 = s.containsDuplicate(nums1)
    assert result1 == expected1, f"Test Case 1 Failed: expected output {expected1}, but got {result1}"
    # Test case 2
    nums2 = [1,2,3,4]
    expected2 = False
    result2 = s.containsDuplicate(nums2)
    assert result2 == expected2, f"Test Case 2 Failed: expected output {expected2}, but got {result2}"
    # Test case 3
    nums3 = [1,1,1,3,3,4,3,2,4,2]
    expected3 = True
    result3 = s.containsDuplicate(nums3)
    assert result3 == expected3, f"Test Case 3 Failed: expected output {expected3}, but got {result3}"