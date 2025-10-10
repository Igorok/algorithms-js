from typing import List
from json import dumps
from collections import defaultdict, deque
import heapq

class Solution_0:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        rainsByLake = defaultdict(int)
        rainsQueue = deque()

        for i in range(n):
            lake = rains[i]
            if lake == 0:
                continue

            rainsByLake[lake] += 1
            if rainsByLake[lake] > 1:
                rainsQueue.append(lake)

        lakeState = defaultdict(int)
        res = []

        for i in range(n):
            lake = rains[i]

            if lake == 0:
                if not rainsQueue:
                    res.append(1)
                    continue

                nextLake = rainsQueue[0]
                if lakeState[nextLake] == 1:
                    lakeState[nextLake] = 0
                    rainsQueue.popleft()
                    res.append(nextLake)
                continue

            if lakeState[lake] == 1:
                return []

            lakeState[lake] += 1
            res.append(-1)

        return res

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        rainsByLake = {}

        for i in range(n):
            lake = rains[i]
            if lake == 0:
                continue

            rainsByLake[lake] = rainsByLake.get(lake, deque())
            rainsByLake[lake].append(i)

        lakeState = defaultdict(int)
        rainsQueue = []
        res = []

        for i in range(n):
            lake = rains[i]

            if lake == 0:
                if not rainsQueue:
                    res.append(1)
                    continue

                id, nextLake = heapq.heappop(rainsQueue)
                lakeState[nextLake] = 0
                res.append(nextLake)
                continue

            if lakeState[lake] == 1:
                return []

            lakeState[lake] += 1
            res.append(-1)

            rainsByLake[lake].popleft()
            if rainsByLake[lake]:
                heapq.heappush(rainsQueue, (rainsByLake[lake][0], lake))


        return res


'''
1 2 0 0 3 0 4 0 4 3 1 2


'''

def test ():
    params = [
        {
            'input': [1,0,2,0,2,1],
            'output': [-1,1,-1,2,-1,-1],
        },
        {
            'input': [1,2,3,4],
            'output': [-1,-1,-1,-1],
        },
        {
            'input': [1,2,0,0,2,1],
            'output': [-1,-1,2,1,-1,-1],
        },
        {
            'input': [1,2,0,1,2],
            'output': [],
        },
        {
            'input': [69,0,0,0,69],
            'output': [-1,69,1,1,-1],
        },
    ]
    solution = Solution()

    for param in params:
        rains = param['input']
        result = solution.avoidFlood(rains)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
