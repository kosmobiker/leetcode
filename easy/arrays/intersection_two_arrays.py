"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and 
you may return the result in any order.
"""
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pass
    
if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    expected1 = [2,2]
    result1 = s.intersect(nums1, nums2)
    assert result1 == expected1, f"Test Case 1 Failed: expected output {expected1}, but got {result1}"

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    expected2 = [4,9] or [9,4]
    result2 = s.containsDuplicate(nums1, nums2)
    assert result2 == expected2, f"Test Case 2 Failed: expected output {expected2}, but got {result2}"
