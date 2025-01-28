class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quick_sel(l, r):
            p, pivot = l, nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p == k:
                return nums[p]
            elif p > k:
                return quick_sel(l, p - 1)
            elif p < k:
                return quick_sel(p + 1, r)
            
        return quick_sel(0, len(nums) - 1)
        