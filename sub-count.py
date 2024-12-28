def countSubstrings(self, s: str) -> int:
        count = 0
        for (i,c) in enumerate(s):
            count += 1
            counter = 1
            actual_w = c
            while (i - counter) >= 0 and (i + counter) < len(s) and (s[i - counter] == s[i + counter]):
                counter += 1
                count += 1
            counter = 1
            if i >= (len(s) - 1) or not s[i + 1] == c:
                continue
            count += 1
            while (i - counter) >= 0 and (i + 1 + counter) < len(s) and (s[i - counter] == s[i + 1 + counter]):
                counter += 1
                count += 1
        return count