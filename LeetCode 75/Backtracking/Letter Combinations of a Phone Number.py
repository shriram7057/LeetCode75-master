class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        phone = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(i, path):
            if i == len(digits):
                result.append(path)
                return
            
            for ch in phone[digits[i]]:
                backtrack(i + 1, path + ch)

        backtrack(0, "")
        return result
