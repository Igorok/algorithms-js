from typing import List
import json
from collections import deque
import heapq

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        shifts = ((-1, 0), (1, 0), (0, -1), (0, 1))

        n = len(grid)
        m = len(grid[0])
        allKeys = set()
        start = [0, 0]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '.' or grid[i][j] == '#':
                    continue
                if grid[i][j] == '@':
                    start = (i ,j)
                    continue
                if grid[i][j] == grid[i][j].lower():
                    allKeys.add(grid[i][j])

        def checkIsPossible():
            myLocks = {}
            myKeys = set()
            visited = set()

            cellQueue = deque()
            cellQueue.append((start[0], start[1]))
            visited.add(start)

            while cellQueue:
                r, c = cellQueue.popleft()

                for sR, sC in shifts:
                    newR = r + sR
                    newC = c + sC

                    if newR == -1 or newR == n or newC == -1 or newC == m:
                        continue
                    if grid[newR][newC] == '#':
                        continue
                    if (newR, newC) in visited:
                        continue

                    val = grid[newR][newC]
                    if val == '.':
                        visited.add((newR, newC))
                        cellQueue.append((newR, newC))
                        continue

                    if val == val.upper():
                        key = val.lower()
                        if key in myKeys:
                            visited.add((newR, newC))
                            cellQueue.append((newR, newC))
                        else:
                            myLocks[key] = (newR, newC)

                    if val == val.lower():
                        myKeys.add(val)
                        if len(myKeys) == len(allKeys):
                            return True

                        if val in myLocks:
                            visited.add(myLocks[val])
                            cellQueue.append(myLocks[val])

                        visited.add((newR, newC))
                        cellQueue.append((newR, newC))

            return False


        def bruteForce():
            cellQueue = deque()
            cellQueue.append((start[0], start[1], 0, set()))
            cache = set()
            cache.add((start[0], start[1], ''))

            while cellQueue:
                r, c, length, keys = cellQueue.popleft()

                r = r

                for sR, sC in shifts:
                    localKeys = keys.copy()
                    newR = r + sR
                    newC = c + sC

                    if newR == -1 or newR == n or newC == -1 or newC == m:
                        continue

                    val = grid[newR][newC]
                    keysList = '_'.join(sorted(list(keys)))

                    if val == '#':
                        continue

                    if (newR, newC, keysList) in cache:
                        continue

                    if val == '.' or val == '@':
                        cellQueue.append((newR, newC, length + 1, localKeys.copy()))
                        cache.add((newR, newC, keysList))
                        continue

                    if val == val.upper():
                        key = val.lower()
                        if key in localKeys:
                            cellQueue.append((newR, newC, length+1, localKeys.copy()))
                            cache.add((newR, newC, keysList))

                    if val == val.lower():
                        localKeys = localKeys.copy()
                        localKeys.add(val)
                        if len(localKeys) == len(allKeys):
                            return length + 1

                        keysList = '_'.join(sorted(list(keys)))
                        cellQueue.append((newR, newC, length+1, localKeys.copy()))
                        cache.add((newR, newC, keysList))

            return -1


        # possible = checkIsPossible()
        # if not possible:
        #     return -1


        return bruteForce()

'''

[
"@.a....",
"###.###",
"b.A.BcC"
]


["@.a....","###.###","b.A.BCc"]


[
"..#....##.",
"....d.#.D#",
"#...#.c...",
"..##.#..a.",
"...#....##",
"#....b....",
".#..#.....",
"..........",
".#..##..A.",
".B..C.#..@"
]






[
"@..aA",
"..B#.",
"....b"
]

'''


def test ():
    params = [

        {
            'input': ["@.a..","###.#","b.A.B"],
            'output': 8,
        },
        {
            'input': ["@..aA","..B#.","....b"],
            'output': 6,
        },
        {
            'input': ["@Aa"],
            'output': -1,
        },
        {
            'input': [
                "@.a....",
                "###.###",
                "b.A.BcC",
            ],
            'output': 13,
        },
        {
            'input': [
                "@.a....",
                "###.###",
                "b.A.BCc",
            ],
            'output': -1,
        },
        {
            'input': ["..#....##.","....d.#.D#","#...#.c...","..##.#..a.","...#....##","#....b....",".#..#.....","..........",".#..##..A.",".B..C.#..@"],
            'output': 19,
        },
    ]

    # ["..#....##.","....d.#.D#","#...#.c...","..##.#..a.","...#....##","#....b....",".#..#.....","..........",".#..##..A.",".B..C.#..@"]

    solution = Solution()

    for param in params:
        result = solution.shortestPathAllKeys(param['input'])
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
