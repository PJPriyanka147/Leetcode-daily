class Solution:
    def check(self, nums: List[int]) -> bool:
        #Function to check if an array is sorted in non-decreasing order
        def is_sorted(arr):
            return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    
        # Generate all rotations and check if any is sorted
        for i in range(len(nums)):
            rotated = nums[i:] + nums[:i]
            if is_sorted(rotated):
                return True
    
        return False


