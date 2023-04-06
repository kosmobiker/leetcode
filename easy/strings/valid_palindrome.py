"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        return True if s == s[::-1] else False
    
if __name__ == '__main__':
    s = Solution()
    
    # Test case 1
    s1 = "A man, a plan, a canal: Panama"
    expected1 = True
    r1 = s.isPalindrome(s1)
    assert r1 == expected1, f"Test Case 1 Failed: expected output {expected1}, but got {r1}"
    
    # Test case 2
    s2 = "race a car"
    expected2 = False
    r2 = s.isPalindrome(s2)
    assert r2 == expected2, f"Test Case 2 Failed: expected output {expected2}, but got {r2}"
    
     # Test case 3
    s3 = " "
    expected3 = True
    r3 = s.isPalindrome(s3)
    assert r3 == expected3, f"Test Case 3 Failed: expected output {expected3}, but got {r3}"