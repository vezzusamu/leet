class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
            t1, t2, t3 = 0, 0, 0
            for triplet in triplets:
                if (target[0] <  triplet[0]) or (target[1] <  triplet[1]) or (target[2] < triplet[2]):
                    continue
                t1 = max(t1, triplet[0])
                t2 = max(t2, triplet[1])
                t3 = max(t3, triplet[2])
            return (t1 == target[0]) and (t2 == target[1]) and (t3 == target[2])