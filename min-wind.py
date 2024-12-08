class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required_chars = {}
        for c in t:
            required_chars[c] = 1 + required_chars.get(c, 0)
        l = 0
        res = ""
        min_len = 0
        for r in range(len(s)):
            if s[r] in required_chars.keys():
                required_chars[s[r]] -= 1
            while all(v < 1 for v in required_chars.values()) and l<=r:
                min_len = min(min_len, r - l + 1)
                res = s[l:r+1]
                if s[l] in required_chars.keys():
                    required_chars[s[l]] += 1
                l += 1
                
        return res
