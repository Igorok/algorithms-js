from typing import List
import json
import heapq

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        steps = (
            (1 ,0),
            (-1 ,0),
            (0 ,1),
            (0 ,-1),
        )

        res = float('inf')

        print('res', res)

        graph = [(0, (0, 0))]
        visited = [[-1]*len(grid[0]) for i in range(len(grid))]

        while len(graph):
            count, loc = heapq.heappop(graph)
            y, x = loc

            print(
                'y', y,
                'x', x,
                'count', count,
                'visited', visited,
                'visited.get((y, x))', visited[y][x],
            )

            if visited[y][x] != -1 and visited[y][x] <= count:
                continue

            visited[y][x] = count



            if y == len(grid) - 1 and x == len(grid[0]) - 1:
                res = min(res, count)

            for i, j in steps:
                stepY = y + i
                stepX = x + j

                if stepY < len(grid) and stepX < len(grid[0]) and stepY > -1 and stepX > -1:
                    if visited[stepY][stepX] == -1 or visited[stepY][stepX] > (count + grid[stepY][stepX]):
                        heapq.heappush(graph, (count + grid[stepY][stepX], (stepY, stepX)))

        return res

'''

[0,1,1],
[1,1,0],
[1,1,0]

'''


def test ():
    params = [
        {
            'input': [[0,1,1],[1,1,0],[1,1,0]],
            'output': 2,
        },
        {
            'input': [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]],
            'output': 0,
        },



    ]
    solution = Solution()

    for param in params:
        result = solution.minimumObstacles(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
