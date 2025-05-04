import heapq
from heapq import heappop, heappush, heapify


class Solution:
    def reorganizeString(self, s: str) -> str:
        c_counts = {}
        ret = ""
        m_heap = []
        heapify(m_heap)
        for c in s:
            current = c_counts.get(c, 0)
            c_counts[c] = 1 + current

        for k in c_counts.keys():
            current_c = c_counts[k]
            m = (-current_c, k)
            heappush(m_heap, m)

        last = None
        for i in range(len(s)):
            m = heappop(m_heap)
            if last == m[1]:
                if not(len(m_heap)):
                    return ""
                m1 = heappop(m_heap)
                if m1 == None:
                    return ""
                else:
                    last = m1[1]
                    ret += m1[1]
                    if m1[0] < -1:
                        m1 = (m1[0] + 1, m1[1])
                        heappush(m_heap, m1)
                    heappush(m_heap, m)
            else:
                last = m[1]
                ret += (m[1])
                if m[0] < -1:
                    m = (m[0] + 1, m[1])
                    heappush(m_heap, m)
            
        return ret