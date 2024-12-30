class Solution:
    def numDecodingsOld(self, s: str) -> int:
        count = 0

        def dfs(i):
            nonlocal count
            if i >= len(s):
                count += 1
                return 
            if s[i] == "0":
                return
            if len(s[i:]) >= 2 and int(s[i:i+2]) <= 26:
                dfs(i + 2)
            dfs(i + 1)
        
        dfs(0)
        return count
    
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if len(s[i:]) >= 2 and int(s[i:i+2]) <= 26:
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)
        