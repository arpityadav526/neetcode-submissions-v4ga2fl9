class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for char in s:
            if char.isalnum():
                chars.append(char.lower())

        i = 0
        j = len(chars) - 1

        while i < j:
            if chars[i] != chars[j]:
                return False
            i += 1
            j -= 1

        return True