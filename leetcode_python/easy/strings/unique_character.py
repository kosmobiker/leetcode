"""
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # counting
        d = dict()
        for char in s:
            if char not in d:
                d[char] = 0
            d[char] += 1
        # filtering
        d = {k: v for (k, v) in d.items() if v == 1}
        if len(d) == 0:
            return -1
        i = 0
        # checking
        for char in s:
            if char == list(d.keys())[0]:
                return i
            i += 1


if __name__ == "__main__":
    s = Solution()

    # Test case 1
    # s1 = "leetcode"
    s1 = "dddccdbba"
    excepted1 = 8
    r1 = s.firstUniqChar(s1)
    assert r1 == excepted1, f"Test Case 1 Failed: expected output {excepted1}, but got {r1}"

    # Test case 2
    s2 = "loveleetcode"
    excepted2 = 2
    r2 = s.firstUniqChar(s2)
    assert r2 == excepted2, f"Test Case 2 Failed: expected output {excepted2}, but got {r2}"

    # Test case 3
    s3 = "aabb"
    excepted3 = -1
    r3 = s.firstUniqChar(s3)
    assert r3 == excepted3, f"Test Case 3 Failed: expected output {excepted3}, but got {r3}"
