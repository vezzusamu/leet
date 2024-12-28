def subset_with_dup(nums):
    ret_vals = [[]]
    for num in nums:
        ret_vals += [sorted(ret_val + [num]) for ret_val in ret_vals if not sorted(ret_val + [num]) in ret_vals]
        
    return ret_vals    
i = 4
l = {}
# create each possible combination of l[i - 1] and l[i - 2] in a single list 
l[i] = [sorted(ret_val + [i]) for ret_val in l[i - 1] + l[i - 2] if not sorted(ret_val + [i]) in l[i - 1] + l[i - 2]]
        