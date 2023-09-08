class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_anagrams = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in str_anagrams:
                str_anagrams[sorted_s].append(s)
            else:
                str_anagrams[sorted_s] = [s]
        return list(str_anagrams.values())