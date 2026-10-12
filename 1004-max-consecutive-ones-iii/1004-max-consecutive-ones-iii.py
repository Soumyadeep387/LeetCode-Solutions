class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        low = 0
        maxL = 0
        zeroC = 0

        for high in range(n):
            if nums[high] == 0:
                zeroC += 1
            while(zeroC > k):
                if nums[low] == 0:
                    zeroC -= 1
                low += 1
            maxL = max(maxL, high - low + 1)
        return maxL