class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        low = 0
        high = 0
        res = float("inf")
        min_sum = 0

        while(high < n):
            min_sum += nums[high]
            while (min_sum >= target):
                ans = high - low + 1
                res = min(ans, res)
                min_sum -= nums[low]
                low += 1
            high += 1
        
        if res == float("inf"):
            return 0
        return res