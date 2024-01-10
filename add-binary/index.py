from typing import List
"""
Given two binary strings a and b, return their sum as a binary string.
https://leetcode.com/problems/add-binary/description/

Input: a = "11", b = "1"
Output: "100"

Binary numbers are two to the power of column number

|  1  |  0  |  1  |  1  |
| 8's | 4's | 2's | 1's |

1011 = 1*8 + 0*4 + 1*2 + 1*1 = 11


Binary Addition
    1 1 1
    1 0 1 1     (8 + 0 + 2 + 1) = 11
  + 1 1 0 1     (8 + 4 + 0 + 1) = 13
    -------
= 1 1 0 0 0 = 16x1 + 8x1 + 4x0 + 2x0 + 1x0 = 24

- In binary, 1+1 = 2, but 2 in binary equals to 10
- carry = sum / 2 = 2/2 = 1
- result = sum % 2 = 2%2 = 0

1 + 1 + 1 = 3 = 1 1 in binary = 2x1 + 1

"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # traverse strings right to left
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        
        result = ""
        while(i>=0 or j>=0 or carry==1):
            # ensure we take carry
            
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1

            # prepend sum modulos 2
            result = str(carry % 2) + result
            # carry over sum divided by two
            carry //= 2
        
        return result

# 100
print(Solution().addBinary("11","1"))
# 11100
print(Solution().addBinary("1111","1101"))
# 10101
print(Solution().addBinary("1010","1011"))