class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        dis_point = {int:List[List[int]]}
        for point in points:
            dis = (point[0] ** 2 + point[1]**2)
            heapq.heappush(heap,dis)
            lis = dis_point.get(dis, [])
            lis.append(point)
            dis_point[dis] = lis
        res = []
        while(k):
            val = heapq.heappop(heap)
            lis = dis_point[val]
            if k < len(lis):
                for l in lis[:k + 1]:
                    res.append(l)
                return res
            for l in lis:
                res.append(l)
            k -= len(lis)
        return res