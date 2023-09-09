class Solution:
    #Quadratic solution
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for point_1 in range(0, len(numbers) - 1):
            point_2 = len(numbers) - 1
            while numbers[point_1] + numbers[point_2] > target and point_1 < point_2:
                point_2 = point_2 - 1
            if numbers[point_1] + numbers[point_2] == target:
                return [point_1 + 1, point_2 + 1]
            
    #Linear solution
    def twoSum_extra(self, numbers: List[int], target: int) -> List[int]:
        hi = len(numbers)-1
        low = 0
        while low<hi:
            if numbers[low]+numbers[hi]>target:
                hi -=1
                continue
            if numbers[low]+numbers[hi] < target:
                low +=1
                continue
            elif numbers[low]+numbers[hi] == target:
                break
        return [low+1,hi+1]