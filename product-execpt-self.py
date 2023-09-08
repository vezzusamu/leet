class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for i in range(len(nums)):
            if(nums[i] == 0):
                zero_count += 1
                continue
            product *= nums[i]
        for i in range(len(nums)):
            if zero_count > 1:
                nums[i] = 0
                continue
            if zero_count == 1:
                if nums[i] == 0:
                    nums[i] = product 
                else:
                    nums[i] = 0
                continue
            nums[i] = int(product / nums[i])
        return nums