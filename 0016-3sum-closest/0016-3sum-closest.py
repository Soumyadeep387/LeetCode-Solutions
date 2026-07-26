class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range (n-2):
            l = i + 1
            r = n - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if abs(sum-target) < abs(closest-target):
                    closest = sum
                if sum == target:
                    return sum
                
                elif sum < target:
                    l += 1
            
                else:
                    r -= 1
        
        return closest    