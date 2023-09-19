class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t = tuple(zip(position, speed))
        t = sorted(t)
        st = []
        for el in reversed(t):
            app_el = (target - el[0]) / el[1]
            if st and st[-1] >= app_el:
                continue
            else:
                st.append(app_el) 

        return len(st)