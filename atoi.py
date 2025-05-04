class Solution:
    def myAtoi(self, s: str) -> int:
        ret = 0
        is_negative = False
        has_started = False
        for c in s:
            if not has_started:
                if c == "-":
                    is_negative = True
                    has_started = True
                    continue
                elif c == "+":
                    has_started = True
                    continue
                elif c == " ":
                    continue
            
            try: 
                val = int(c)                
                ret *= 10
                ret += val
                has_started = True
            except:
                break
        ret = ret if not is_negative else -ret
        ret = max(ret, - pow(2, 31))
        ret = min(ret, pow(2, 31) - 1)
        return ret