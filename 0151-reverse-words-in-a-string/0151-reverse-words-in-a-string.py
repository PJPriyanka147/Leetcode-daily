class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()

        words = s.split()

        words.reverse()

        reversed_s = ' '.join(words)

        return reversed_s