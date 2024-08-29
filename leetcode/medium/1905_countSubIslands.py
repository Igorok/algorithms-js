from typing import List

class Solution:
    def getDfs(self, grid, visited):
        def dfs(x, y, island):
            if y == len(grid) or y < 0 or x == len(grid[0]) or x < 0 or grid[y][x] == 0 or (x,y) in visited:
                return

            visited.add((x, y))
            island.append((x, y))

            neighbours = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y),]
            for nei in neighbours:
                dfs(nei[0], nei[1], island)

        return dfs

    def markIslands(self, grid):
        visited = set()
        islands = [[0]*len(grid[0]) for i in range(len(grid))]

        dfs = self.getDfs(grid, visited)

        i = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1 and (x, y) not in visited:
                    i += 1
                    island = []
                    dfs(x, y, island)
                    for v in island:
                        islands[v[1]][v[0]] = i


        return islands

    def checkIslands(self, grid, markedIslands):
        visited = set()
        islands = [[0]*len(grid[0]) for i in range(len(grid))]

        dfs = self.getDfs(grid, visited)

        def checkIsland(island):
            x0, y0 = island[0]
            id = markedIslands[y0][x0]
            if id == 0:
                return False

            for i in range(1, len(island)):
                x, y = island[i]
                if markedIslands[y][x] != id:
                    return False

            return True

        i = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1 and (x, y) not in visited:
                    island = []
                    dfs(x, y, island)
                    if checkIsland(island):
                        i += 1

        return i


    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        markedIslands = self.markIslands(grid1)

        print('markedIslands', markedIslands)
        # print('islands2', islands2)

        return self.checkIslands(grid2, markedIslands)


'''

[
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0],
    [2, 2, 0, 3, 3]
]








'''



def test ():
    params = [
        {
            'input': [
                [
                    [1,1,1,0,0],
                    [0,1,1,1,1],
                    [0,0,0,0,0],
                    [1,0,0,0,0],
                    [1,1,0,1,1]
                ],
                [
                    [1,1,1,0,0],
                    [0,0,1,1,1],
                    [0,1,0,0,0],
                    [1,0,1,1,0],
                    [0,1,0,1,0]
                ],
            ],
            'output': 3,
        },
        {
            'input': [
                [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
                [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
            ],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        grid1, grid2 = param['input']
        result = solution.countSubIslands(grid1, grid2)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
