"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
from typing import List

class Solution:
    #Kolhoz edition
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            if num in d:
                d[num] += 1
        for key, value in d.items():
            if value == 1:
                return key
            
    # Cool solution from Leetcode
    # def singleNumber(self, nums: List[int]) -> int:
    #     xor = 0
    #     for num in nums:
    #         xor ^= num
    #     return xor
    
    # Extremely cool solution from Leetcode
    # def singleNumber(self, nums: List[int]) -> int:
    #     return 2*sum(set(nums)) - sum(nums)
        

if __name__ == '__main__':
    s = Solution()
    
    # Test case 1
    nums1 = [2,2,1]
    expected1 = 1
    r1 = s.singleNumber(nums1)
    assert r1 == expected1, f"Test Case 1 Failed: expected output {expected1}, but got {r1}"

    # Test case 2
    nums2 = [4,1,2,1,2]
    expected2 = 4
    r2 = s.singleNumber(nums2)
    assert r2 == expected2, f"Test Case 2 Failed: expected output {expected2}, but got {r2}"

    # Test case 3
    nums3 = [1]
    expected3 = 1
    r3 = s.singleNumber(nums3)
    assert r3 == expected3, f"Test Case 3 Failed: expected output {expected3}, but got {r3}"
  
