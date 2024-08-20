# https://leetcode.com/problems/palindrome-number/

class Solution:
    # without using string or list method
    def is_Palindrome(self, x: int) -> bool:
        temp = x
        reversed_digit = 0
        while temp > 0:
            reversed_digit = reversed_digit * 10 + int(temp % 10)
            temp //= 10
        if reversed_digit == x:
            return True
        return False
