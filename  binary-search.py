class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binSearchAux(nums, target, 0, len(nums) - 1)


    def binSearchAux(self, nums: List[int], target: int, startingIndex: int, endingIndex: int) -> int:
        if startingIndex > endingIndex:
            return -1
        currentIndex = int((startingIndex + endingIndex) / 2)
        if nums[currentIndex] > target:
            return self.binSearchAux(nums, target, startingIndex, currentIndex - 1)
        elif nums[currentIndex] < target:
            return self.binSearchAux(nums, target, currentIndex + 1, endingIndex)
        else:
            return currentIndex