"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, temp = [], ''
        
        self.length = len(digits)
        self.ref = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        return self.helper(digits, res, temp) if digits else []
        
        
    def helper(self, digits, res, temp):
            
        if len(temp) == self.length or not digits:
            res.append(temp)
            return res

        for item in self.ref[digits[0]]:
            self.helper(digits[1:], res, temp+item)

        return res
            
            