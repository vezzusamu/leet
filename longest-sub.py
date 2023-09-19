class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        sub = s[0]
        i = 0
        j = 1
        l = 0
        n = len(s)
        while j < n and i < n:
            if s[j] in sub:
                l = max(len(sub), l)
                i = i + 1
                sub = s[i:j]
                continue
            sub = sub + s[j]
            j = j + 1
        return max(l, len(sub))
        