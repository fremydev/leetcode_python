class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        for i in range(len(s)):
            if i < len(s) - 1 and roman_int[s[i]] < roman_int[s[i + 1]]:
                result = result - roman_int[s[i]]
            else:
                result = result + roman_int[s[i]]

        return result
