class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        top_k = sorted(freq.items(), key=lambda it: it[1], reverse=True)
        top_k = list(map(lambda it: it[0], top_k))
        return top_k[:k]
