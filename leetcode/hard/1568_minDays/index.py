from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def dfs(i, j, visited):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i,j) in visited or grid[i][j] == 0:
                return
            visited.add((i, j))
            neighbor = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for y, x in neighbor:
                dfs(y, x, visited)

        def get_count():
            visited = set()
            count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        dfs(i, j, visited)
                        count += 1
            return count

        if get_count() != 1:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1):
                    grid[i][j] = 0
                    if get_count() != 1:
                        return 1
                    grid[i][j] = 1

        return 2



def test ():
    params = [
        {
            'input': [[0,1,1,0],[0,1,1,0],[0,0,0,0]],
            'output': 2,
        },
        {
            'input': [[1,1]],
            'output': 2,
        },
        {
            'input': [[1,0,1,0]],
            'output': 0,
        },
        {
            'input': [[1,0,0],[1,1,0],[1,0,0]],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minDays(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
