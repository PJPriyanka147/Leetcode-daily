class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pref_count = defaultdict(int)
        pref_count[0] = 1
        odd_count, ans = 0, 0
        for num in nums:
            odd_count += num%2
            if odd_count - k in pref_count:
                ans += pref_count[odd_count - k]
            pref_count[odd_count] += 1
        return ans