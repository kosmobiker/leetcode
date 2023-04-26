"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)
        if c1 == c2:
            return True
        return False
    
if __name__ == '__main__':
    s = Solution()
    
    # Test case 1
    s1 = "anagram"
    t1 = "nagaram"
    excepted1 = True
    r1 = s.isAnagram(s1, t1)
    assert r1 == excepted1, f"Test Case 1 Failed: expected output {excepted1}, but got {r1}"
    
    # Test case 2
    s2 = "rat"
    t2 = "car"
    excepted2 = False
    r2 = s.isAnagram(s2, t2)
    assert r2 == excepted2, f"Test Case 1 Failed: expected output {excepted2}, but got {r2}"