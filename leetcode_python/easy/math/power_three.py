"""
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x.
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n //= 3
        return True


if __name__ == "__main__":
    s = Solution()

    # Test case 1
    n = 27
    e = True
    r = s.isPowerOfThree(n)
    assert r == e, f"Test Case 1 Failed: expected output {e}, but got {r}"

    # Test case 2
    n = 0
    e = False
    r = s.isPowerOfThree(n)
    assert r == e, f"Test Case 2 Failed: expected output {e}, but got {r}"

    # Test case 3
    n = -1
    e = False
    r = s.isPowerOfThree(n)
    assert r == e, f"Test Case 3 Failed: expected output {e}, but got {r}"
