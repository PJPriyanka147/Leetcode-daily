class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
        
            if nums[mid] == target: 
                return True
        
            # If we encounter duplicates, just move the pointers
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
        
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else: 
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
    
        return False
