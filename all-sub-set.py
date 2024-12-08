from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret_vals = [[]]
        
        for num in nums:
            print(ret_vals)
            ret_vals += [ret_val + [num] for ret_val in ret_vals]
            
        return ret_vals    
        