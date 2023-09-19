class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_temps = []
        ret = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack_temps and temperatures[i] >= temperatures[stack_temps[-1]]:
                ret[stack_temps[-1]] = i - stack_temps[-1]
                stack_temps.pop()
            stack_temps.append(i)

        return ret
        
def dailyTemperatures_old(self, temperatures: List[int]) -> List[int]:
        for i in range(len(temperatures)):
            changed = False
            for j in range(i, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    temperatures[i] = j - i
                    changed = True
                    break
            if not changed:
                temperatures[i] = 0
        return temperatures