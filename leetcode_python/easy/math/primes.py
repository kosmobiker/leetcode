"""
Given an integer n, return the number of prime numbers that are strictly less than n.
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        A = [True] * (n + 1)
        for i in range(2, int(n ** 0.5) + 1):
            if A[i]:
                for j in range(i * i, n + 1, i):
                    A[j] = False
        return sum([1 for i in range(2, n) if A[i]])

if __name__ == '__main__':
    s = Solution()

    # Test case 1
    n = 10
    e = 4
    r = s.countPrimes(n)
    assert r == e, f"Test Case 1 Failed: expected output {e}, but got {r}"

    # Test case 2
    n = 0
    e = 0
    r = s.countPrimes(n)
    assert r == e, f"Test Case 2 Failed: expected output {e}, but got {r}"

    # Test case 3
    n = 1
    e = 0
    r = s.countPrimes(n)
    assert r == e, f"Test Case 3 Failed: expected output {e}, but got {r}"

    # Test case 4
    n = 100_000
    e = 9592
    r = s.countPrimes(n)
    assert r == e, f"Test Case 4 Failed: expected output {e}, but got {r}"