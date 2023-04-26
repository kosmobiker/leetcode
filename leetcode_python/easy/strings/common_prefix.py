"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        prefix = ""
        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                prefix += first[i]
            else:
                break
        return prefix
                
        
if __name__ == '__main__':
    s = Solution()
    
    # Test case 1
    strs1 = ["flower","flow","flight"]
    expected1 = "fl"
    r1 = s.longestCommonPrefix(strs1)
    assert r1 == expected1, f"Test Case 1 Failed: expected output {expected1}, but got {r1}"
    
    # Test case 2
    strs2 = ["dog","racecar","car"]
    expected2 = ""
    r2 = s.longestCommonPrefix(strs2)
    assert r2 == expected2, f"Test Case 2 Failed: expected output {expected2}, but got {r2}" 
   
    # Test case 3
    strs3 = [""]
    expected3 = ""
    r3 = s.longestCommonPrefix(strs3)
    assert r3 == expected3, f"Test Case 3 Failed: expected output {expected3}, but got {r3}"     