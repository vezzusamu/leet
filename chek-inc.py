import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_set = collections.Counter(s1)
        for i in range(len(s2) - len(s1)+ 1):
            s2_set = collections.Counter(s2[i:i+len(s1)])
            if s1_set == s2_set:
                return True
        return False