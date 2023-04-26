"""
Given two strings needle and haystack, return the index of the first occurrence 
of needle in haystack, or -1 if needle is not part of haystack.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        for i in range(h - n + 1):
            if haystack[i: n + i] == needle:
                return i
        return -1
        
        # # elegant solution from leetcode
        # return haystack.find(needle)
    
if __name__ == '__main__':
    s = Solution()
    
    # Test case 1
    haystack1 = "sadbutsad"
    needle1 = "sad"
    expected1 = 0
    r1 = s.strStr(haystack1, needle1)
    assert r1 == expected1, f"Test Case 1 Failed: expected output {expected1}, but got {r1}"
    
    # Test case 2
    haystack2 = "leetcode"
    needle2 = "leeto"
    expected2 = -1
    r2 = s.strStr(haystack2, needle2)
    assert r2 == expected2, f"Test Case 2 Failed: expected output {expected2}, but got {r2}"