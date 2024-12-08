class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        steps = []
        for i, el in enumerate(nums):
            while( q and el > q[-1][0]):
                q.pop()
            q.append((el, i))
            print(q)
            if( i < k - 1):
                continue
            print(q[0][1])
            print(i - k)
            while (q[0][1] <= i - k):
                q.popleft()
            max_el = q[0]
            steps.append(max_el[0])

        return steps