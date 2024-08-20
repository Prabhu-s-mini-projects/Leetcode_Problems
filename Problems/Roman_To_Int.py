# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def roman_to_int(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        number = 0
        next_digit_count = False
        for i in range(len(s) - 1):
            if not next_digit_count and i == len(s) - 1:
                number += roman_dict.get(s[i])
                break
            elif int(roman_dict.get(s[i + 1])) > int(roman_dict.get(s[i])):
                number += roman_dict.get(s[i + 1]) - roman_dict.get(s[i])
                next_digit_count = True
            else:
                number += roman_dict.get(s[i + 1])
                next_digit_count = False
        return number
