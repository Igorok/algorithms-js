from typing import List
from json import dumps
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        n = len(buildings)
        buildingsQueue = [(0, float('inf'))]
        id = 0
        m = -1
        while id < n and buildings[id][0] == buildings[0][0]:
            m = max(m, buildings[id][2])
            heapq.heappush(buildingsQueue, (-buildings[id][2], buildings[id][1]))
            id += 1

        res = [
            (buildings[0][0], m)
        ]

        while id < n:
            x, x2, y = buildings[id]
            id += 1

            while buildingsQueue[0][1] < x:
                prevY, prevX = heapq.heappop(buildingsQueue)
                prevY = -prevY

                while buildingsQueue[0][1] <= prevX:
                    heapq.heappop(buildingsQueue)

                if prevY != -buildingsQueue[0][0]:
                    res.append((prevX, -buildingsQueue[0][0]))

            heapq.heappush(buildingsQueue, (-y, x2))
            if (res[-1][1] < -buildingsQueue[0][0]):
                res.append((x, -buildingsQueue[0][0]))


        while len(buildingsQueue) > 1:
            prevY, prevX = heapq.heappop(buildingsQueue)
            prevY = -prevY

            if prevX <= res[-1][0]:
                continue

            while buildingsQueue[0][1] <= prevX:
                heapq.heappop(buildingsQueue)

            if prevY != -buildingsQueue[0][0]:
                res.append((prevX, -buildingsQueue[0][0]))


        return res


'''

ERROR input
[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]] output
[[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]] result
[(2, 10), (3, 15),          (12, 0), (15, 10), (20, 8), (24, 0)]

'''





def test ():
    params = [
        {
            'input': [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]],
            'output': [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]],
        },
        {
            'input': [[0,2,3],[2,5,3]],
            'output': [[0,3],[5,0]],
        },
        {
            'input': [[0,2147483647,2147483647]],
            'output': [[0,2147483647],[2147483647,0]],
        },
        {
            'input': [[2,9,10],[9,12,15]],
            'output': [[2,10],[9,15],[12,0]],
        },
        {
            'input': [[1,2,1],[1,2,2],[1,2,3]],
            'output': [[1,3],[2,0]],
        },
    ]

    solution = Solution()
    for param in params:
        result = solution.getSkyline(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
