"""
Implement the myAtoi(string s) function, which converts a string to 
a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

    1. Read in and ignore any leading whitespace.
    2. Check if the next character (if not already at the end of the string) is '-' or '+'. 
    Read this character in if it is either. This determines if the final result is negative or positive 
    respectively. Assume the result is positive if neither is present.
    3. Read in next the characters until the next non-digit character or the end of the input is reached. 
    The rest of the string is ignored.
    4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, 
    then the integer is 0. Change the sign as necessary (from step 2).
    5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], 
    then clamp the integer so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, 
    and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
    6. Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        m = 1
        if len(s)> 0 and (s[0] == '-' or s[0] == '+'):
            if s[0] == '-':
                m = -1
            s = s[1:]
        elif len(s)> 0 and s[0] == '+':
            m = 1
            s = s[1:]
        else: m = 1
        digits = ""
        for char in s:
            if char.isdigit():
                digits += char
            else:
                break
        if len(digits) > 0:
            digits = m * int(digits)
        else:
            digits = 0
        if digits > 2**31 - 1:
            return 2**31 - 1
        elif digits < -2**31:
            return -2**31
        else:
            return digits
        
            
if __name__ == '__main__':
    s = Solution()
    
    # Test case 1
    s1 = "42"
    expected1 = 42
    r1 = s.myAtoi(s1)
    assert r1 == expected1, f"Test Case 1 Failed: expected output {expected1}, but got {r1}"
    
    # Test case 2
    s2 = "   -42"
    expected2 = -42
    r2 = s.myAtoi(s2)
    assert r2 == expected2, f"Test Case 2 Failed: expected output {expected2}, but got {r2}"
    
     # Test case 3
    s3 = "4193 with words"
    expected3 = 4193
    r3 = s.myAtoi(s3)
    assert r3 == expected3, f"Test Case 3 Failed: expected output {expected3}, but got {r3}"
    
    # Test case 4
    s4 = "-91283472332"
    expected4 = -2147483648
    r4 = s.myAtoi(s4)
    assert r4 == expected4, f"Test Case 4 Failed: expected output {expected4}, but got {r4}"