from typing import List
import json
import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        steps = ((1, 0), (-1, 0), (0, 1), (0, -1))
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        height = len(grid)
        width = len(grid[0])
        visited = [[-1]*width for i in range(height)]
        res = float('inf')
        queue = [(0, 0, 0)]

        while len(queue):
            time, y, x = heapq.heappop(queue)

            if visited[y][x] != -1:
                continue

            print(
                'y', y,
                'x', x,
                'time', time,
            )

            if y == height - 1 and x == width - 1:
                return time

            for i, j in steps:
                stepY = y + i
                stepX = x + j

                if stepY < 0 or stepY == height or stepX < 0 or stepX == width or visited[stepY][stepX] != -1:
                    continue

                nextTime = time + 1
                if grid[stepY][stepX] > nextTime:
                    # if x == 0 and y == 0:
                    #     continue

                    cellDiff = grid[stepY][stepX] - time
                    cellDiff += 1 if (cellDiff % 2) == 0 else 0
                    nextTime = time + cellDiff


                visited[y][x] = time
                heapq.heappush(queue, (nextTime, stepY, stepX))





        return -1

'''

[
[0,1,3,2],
[5,1,2,5],
[4,3,8,6]]

0-1-1-2-3-2-5-6
7

[0,2,1,1],
[1,2,3,1],
[1,1,4,6]

0-1-1-1-4-6
5



[0,1,6,1],
[1,1,8,1],
[1,1,8,6]

0-1-1-1-1-1-1-1-1-8-6



1 3, diff = 2
b,f,go = 3 steps
1 4, diff = 3
b,f,go = 3 steps

+1 step for even difference


'''


def test ():
    params = [
        {
            'input': [[0,1,3,2],[5,1,2,5],[4,3,8,6]],
            'output': 7,
        },
        {
            'input': [[0,2,4],[3,2,1],[1,0,4]],
            'output': -1,
        },
        {
            'input': [
                [0,2,1,1],
                [1,2,3,1],
                [1,1,4,6]
            ],
            'output': 7,
        },
        {
            'input': [
                [0,1,6,1],
                [1,1,8,1],
                [1,1,8,6],
            ],
            'output': 9,
        },
        {
            'input': [
                [0, 1,99],
                [3,99,99],
                [4, 5, 6]
            ],
            'output': 6,
        },

    ]
    solution = Solution()

    for param in params:
        result = solution.minimumTime(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
