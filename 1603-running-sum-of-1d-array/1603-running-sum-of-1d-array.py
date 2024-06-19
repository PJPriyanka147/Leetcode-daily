class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        #create a new list that contains the same elements as nums but is a         different object in memory.
        running_sum = nums[:]

        for i in range(1, len(nums)):
            running_sum[i] = running_sum[i - 1] + running_sum[i]
        
        return running_sum