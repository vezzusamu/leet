def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ret_val = []
        if target == 0:
            return [[]]
        if target < 0:
            return None
        for num in nums:
            nums_r = nums.copy()
            nums_r.remove(num)
            val = self.combinationSum2( nums_r, target - num)
            if val is None:
                continue
            for v in val:
                v.append(num)
                v = sorted(v)
                if not v in ret_val:
                    ret_val.append(v)
        return ret_val