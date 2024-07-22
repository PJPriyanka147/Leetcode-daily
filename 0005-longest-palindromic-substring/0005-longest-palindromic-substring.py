class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(substring: str) -> bool:
            return substring == substring[::-1]

        n = len(s)
        if n == 0:
            return ""

        longest = ""

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if is_palindrome(substring) and len(substring) > len(longest):
                    longest = substring

        return longest