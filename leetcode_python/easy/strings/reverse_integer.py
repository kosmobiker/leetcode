"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer 
range [-2^31, 2^31 - 1], then return 0.
"""
class Solution:
    def reverse(self, x: int) -> int:
        m = -1 if x < 0 else 1
        tmp = []
        x = abs(x)
        while x > 0:
            tmp.append(x % 10)
            x = x // 10
        n = len(tmp) - 1
        x = 0
        while n >= 0:
            x += tmp.pop(0) * 10**n
            n -= 1
        output =  x * m
        if output > 2**31 - 1 or output < -2**31:
            return 0
        return output
    
        
if __name__ == '__main__':
    s = Solution()
    
    # Test case 1
    x1 = 123
    expected1 = 321
    r1 = s.reverse(x1)
    assert r1 == expected1, f"Test Case 1 Failed: expected output {expected1}, but got {r1}"
    
    # Test case 2
    x2 = -123
    expected2 = -321
    r2 = s.reverse(x2)
    assert r2 == expected2, f"Test Case 2 Failed: expected output {expected2}, but got {r2}"
    
    # Test case 3
    x3 = 120
    expected3 = 21
    r3 = s.reverse(x3)
    assert r3 == expected3, f"Test Case 3 Failed: expected output {expected3}, but got {r3}"
    
    # Test case 4
    x4 = 1534236469
    expected4 = 0
    r4 = s.reverse(x4)
    assert r4 == expected4, f"Test Case 4 Failed: expected output {expected4}, but got {r4}"
