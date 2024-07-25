class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        start = 0
        for i in range(len(nums)):
            if i == 0  or nums[i] != nums[i - 1]:
                start = 0
            end= len(res)
            for j in range(start, end):
                res.append(res[j] + [nums[i]])
            start = end
        return res