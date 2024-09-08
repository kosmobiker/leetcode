"""
Given a roman numeral, convert it to an integer.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        s = s[::-1]
        result = roman[s[0]]
        for i in range(1, len(s)):
            if roman[s[i]] >= roman[s[i - 1]]:
                result += roman[s[i]]
            else:
                result -= roman[s[i]]
        return result


if __name__ == "__main__":
    s = Solution()

    # Test case 1
    s1 = "III"
    e = 3
    r = s.romanToInt(s1)
    assert r == e, f"Test Case 1 Failed: expected output {e}, but got {r}"

    # Test case 2
    s2 = "LVIII"
    e = 58
    r = s.romanToInt(s2)
    assert r == e, f"Test Case 2 Failed: expected output {e}, but got {r}"

    # Test case 3
    s3 = "MCMXCIV"
    e = 1994
    r = s.romanToInt(s3)
    assert r == e, f"Test Case 3 Failed: expected output {e}, but got {r}"
