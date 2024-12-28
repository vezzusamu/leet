class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_l = 0
        best_w = None
        for (i,c) in enumerate(s):
            counter = 1
            actual_w = c
            while (i - counter) >= 0 and (i + counter) < len(s) and (s[i - counter] == s[i + counter]):
                actual_w = s[i - counter] + actual_w + s[i + counter]
                counter += 1
            if len(actual_w) > best_l:
                best_l = len(actual_w)
                best_w = actual_w
            counter = 1
            if i >= (len(s) - 1) or not s[i + 1] == c:
                continue
            actual_w = c + s[i+1]
            while (i - counter) >= 0 and (i + 1 + counter) < len(s) and (s[i - counter] == s[i + 1 + counter]):
                actual_w = s[i - counter] + actual_w + s[i + 1 + counter]
                counter += 1
            if len(actual_w) > best_l:
                best_l = len(actual_w)
                best_w = actual_w
        return best_w
                
        