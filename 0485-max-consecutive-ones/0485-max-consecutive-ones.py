class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_ones = 0

        for num in nums:
            if num ==  1:
                current_ones += 1
            else:
                if current_ones > max_ones:
                    max_ones = current_ones
                current_ones = 0

        if current_ones > max_ones:
            max_ones = current_ones

        return max_ones


            