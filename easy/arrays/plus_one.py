"""
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. The digits are ordered 
from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # nice version
        n = len(digits)
        number = 0
        # get initial number
        for i in range(n):
            number += digits[i] * (10 ** (n - i - 1)) 
        # plus one
        number += 1
        # now it's the other way around
        digits = []
        while number > 0:
            digits.append(number % 10)
            number //= 10
        digits.reverse()
        return digits

        # # cheat version :-)
        # number = int(''.join(map(str, digits)))
        # number += 1
        # digits = [int(digit) for digit in str(number)]
        # return digits
        
        
    
if __name__ == '__main__':
    s = Solution()
    
    # Test case 1
    digits1 = [1,2,3]
    expected1 = [1,2,4]
    r1 = s.plusOne(digits1)
    assert r1 == expected1, f"Test Case 1 Failed: expected output {expected1}, but got {r1}"
    
    # Test case 2
    digits2 = [4,3,2,1]
    expected2 = [4,3,2,2]
    r2 = s.plusOne(digits2)
    assert r2 == expected2, f"Test Case 2 Failed: expected output {expected2}, but got {r2}"
    
    # Test case 3
    digits3 = [9]
    expected3 = [1,0]
    r3 = s.plusOne(digits3)
    assert r3 == expected3, f"Test Case 3 Failed: expected output {expected3}, but got {r3}"
