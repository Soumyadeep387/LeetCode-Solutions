class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        id = 0
        res = [0] * (m + n)
        while(i < m and j < n):
            if(nums1[i] <= nums2[j]):
                res[id] = nums1[i]
                id += 1
                i += 1
            else:
                res[id] = nums2[j]
                id += 1
                j += 1
        
        while(j < n):
           res[id] = nums2[j]
           id += 1
           j += 1
        
        while (i < m):
            res[id] = nums1[i]
            id += 1
            i += 1

        nums1[:] = res  
        

        