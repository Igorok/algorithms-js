from typing import List
from json import dumps
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])

        if m < 3 or n < 3:
            return 0

        borderOffset = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def isInvalid(y, x):
            return y < 0 or x < 0 or y >= m or x >= n

        visited = [[0]*n for i in range(m)]

        borderQueue = []

        for i in range(m):
            heapq.heappush(borderQueue, (heightMap[i][0], i, 0))
            heapq.heappush(borderQueue, (heightMap[i][n-1], i, n-1))
            visited[i][0] = 1
            visited[i][n-1] = 1

        for i in range(n):
            heapq.heappush(borderQueue, (heightMap[0][i], 0, i))
            heapq.heappush(borderQueue, (heightMap[m-1][i], m-1, i))
            visited[0][i] = 1
            visited[m-1][i] = 1

        res = 0
        while borderQueue:
            h, i, j = heapq.heappop(borderQueue)
            visited[i][j] = 2

            for addY, addX in borderOffset:
                y = i + addY
                x = j + addX
                if isInvalid(y, x) or visited[y][x] != 0:
                    continue
                if heightMap[y][x] < h:
                    res += h - heightMap[y][x]
                    heightMap[y][x] = h

                if visited[y][x] == 0:
                    visited[y][x] = 1
                    heapq.heappush(borderQueue, (heightMap[y][x], y, x))

        return res

'''

[1,4,3,1,3,2],
[3,2,1,3,2,4],
[2,3,3,2,3,1]



0 1 2 1 0
0 1 3 1 0
0 1 2 1 0



0 0 0 0 0
1 1 1 1 1
3 2 1 2 3
3 2 0 2 3
3 2 0 2 3
3 2 1 2 3
1 1 1 1 1


2 2 2
2 2 2
2 1 2
2 1 2
2 1 2
2 0 2


'''

def test ():
    params = [
        {
            'input': [
                [1,4,3,1,3,2],
                [3,2,1,3,2,4],
                [2,3,3,2,3,1]
            ],
            'output': 4,
        },
        {
            'input': [
                [3,3,3,3,3],
                [3,2,2,2,3],
                [3,2,1,2,3],
                [3,2,2,2,3],
                [3,3,3,3,3]
            ],
            'output': 10,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.trapRainWater(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
