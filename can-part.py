class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if(target % 2):
            return False
        target = target // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1 , -1):
            nextDP = set()
            print(dp)
            for d in dp:
                if (nums[i] + d) == target:
                    return True
                nextDP.add(nums[i] + d)
                nextDP.add(d)
            dp = nextDP
        return False