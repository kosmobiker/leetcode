"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        
if __name__ == '__main__':
    s = Solution()
    
    # Test case 1
    s1 = ["h","e","l","l","o"]
    expected1 = ["o","l","l","e","h"]
    s.reverseString(s1)
    assert s1 == expected1, f"Test Case 1 Failed: expected output {expected1}, but got {s1}"
    
    # Test case 1
    s2 = ["H","a","n","n","a","h"]
    expected2 = ["h","a","n","n","a","H"]
    s.reverseString(s2)
    assert s2 == expected2, f"Test Case 1 Failed: expected output {expected2}, but got {s2}"

    