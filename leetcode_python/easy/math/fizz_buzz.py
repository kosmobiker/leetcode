"""
Given an integer n, return a string array answer (1-indexed) where:

- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i (as a string) if none of the above conditions are true.
"""
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1, n + 1):
            if (i % 3 == 0) & (i % 5 == 0):
                output.append("FizzBuzz")
            elif i % 3 == 0:
                output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(i))
        return output

if __name__ == '__main__':
    s = Solution()

    # Test case 1
    n1 = 3
    expected1 = ["1","2","Fizz"]
    r1 = s.fizzBuzz(n1)
    assert r1 == expected1, f"Test Case 1 Failed: expected output {expected1}, but got {r1}"

    # Test case 2
    n2 = 5
    expected2 = ["1","2","Fizz","4","Buzz"]
    r2 = s.fizzBuzz(n2)
    assert r2 == expected2, f"Test Case 2 Failed: expected output {expected2}, but got {r2}"

    # Test case 3
    n3 = 15
    expected3 = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    r3 = s.fizzBuzz(n3)
    assert r3 == expected3, f"Test Case 3 Failed: expected output {expected3}, but got {r3}"