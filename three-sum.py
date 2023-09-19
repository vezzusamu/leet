class Solution:
    def threeSum_one_for_check(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums = sorted(nums)
        zero_count = 0
        elements = {}

        for i in range(len(nums)):
            if(nums[i] == 0):
                zero_count = zero_count + 1
                if zero_count > 1:
                    continue
            if(nums[i] in elements):
                elements[nums[i]] = elements[nums[i]] + 1
            else:
                elements[nums[i]] =  1

        
        if(zero_count > 2):
            ret.add((0,0,0))

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                checked_number =  -(nums[i] + nums[j])
                if checked_number in elements:
                    if checked_number == nums[i] or checked_number == nums[j]:
                        if elements[checked_number] < 2:
                            continue
                    append_val = tuple(sorted((nums[i], nums[j],checked_number)))
                    ret.add(append_val)
        return ret
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums = sorted(nums)
        zero_count = 0
        positives = []
        negatives = []

        for i in range(len(nums)):
            if(nums[i] == 0):
                zero_count = zero_count + 1
                if zero_count == 1:
                    negatives.append(0)
            elif (nums[i] < 0):
                negatives.append(nums[i])
            else:
                positives.append(nums[i])
        
        if(zero_count > 2):
            ret.add((0,0,0))
        p = set(positives)
        n = set(negatives)

        for i in range(len(negatives)):
            for j in range(i + 1, len(negatives)):
                checked_number =  -(negatives[i] + negatives[j])
                if checked_number in p:
                    append_val = (negatives[i], negatives[j],checked_number)
                    ret.add(append_val)

        
        for i in range(len(positives)):
            for j in range(i + 1, len(positives)):
                checked_number =  -(positives[i] + positives[j])
                if checked_number in n:
                    append_val = (positives[i], positives[j],checked_number)
                    ret.add(append_val)

        
        return ret
                    
                    
