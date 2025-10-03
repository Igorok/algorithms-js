from typing import List
from json import dumps
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        shifts = ((-1, 0), (1, 0), (0,-1), (0, 1))
        height = len(heightMap)
        width = len(heightMap[0])

        visited = [[0] * width for _ in range(height)]
        borders = []

        for row in range(height):
            heapq.heappush(borders, (heightMap[row][0], row, 0))
            heapq.heappush(borders, (heightMap[row][width-1], row, width-1))
            visited[row][0] = 1
            visited[row][width-1] = 1

        for col in range(1, width-1):
            heapq.heappush(borders, (heightMap[0][col], 0, col))
            heapq.heappush(borders, (heightMap[height-1][col], height-1, col))
            visited[0][col] = 1
            visited[height-1][col] = 1

        def isInvalidCell(row, col):
            return row < 0 or row == height or col < 0 or col == width or visited[row][col] == 1

        def dfs(row, col, border):
            if isInvalidCell(row, col):
                return 0

            visited[row][col] = 1
            val = heightMap[row][col]
            if val >= border:
                heapq.heappush(borders, (val, row, col))
                return 0

            res = border - val

            for sR, sC in shifts:
                newR = row + sR
                newC = col + sC
                res += dfs(newR, newC, border)

            return res

        res = 0

        while borders:
            val, row, col = heapq.heappop(borders)

            for sR, sC in shifts:
                newR = row + sR
                newC = col + sC
                res += dfs(newR, newC, val)


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
