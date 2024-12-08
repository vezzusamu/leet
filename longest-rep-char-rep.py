class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(count[s[r]], max_freq)
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res