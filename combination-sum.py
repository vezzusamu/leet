class Solution:

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret_val = []
        if target == 0:
            return [[]]
        if target < 0:
            return None
        for num in nums:
            val = self.combinationSum([n for n in nums if n >= num], target - num)
            if val is None:
                continue
            for v in val:
                v.append(num)
                ret_val.append(v)
        return ret_val
