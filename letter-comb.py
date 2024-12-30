class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d_t_l =  {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        curr = {0:[""], -1:[""]}
        if not digits:
            return []
        def dfs(i):
            if i >= len(digits):
                curr[i-1] = [c for c in curr[i-1] if not c == '']
                return curr[i-1]
            for n in d_t_l[digits[i]]:
                for el in curr[i-1]:
                    if not i in curr:
                        curr[i] = []
                    el += n
                    if len(el) <= i:
                        continue
                    curr[i].append(el)
            return dfs(i+1)
                
        
        return dfs(0)