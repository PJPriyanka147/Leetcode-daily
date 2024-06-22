class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        
        original_no = x
        reversed_no = 0

        while x > 0:
            remainder = x % 10
            reversed_no = reversed_no * 10 + remainder
            x = x // 10
        
        return original_no == reversed_no
        