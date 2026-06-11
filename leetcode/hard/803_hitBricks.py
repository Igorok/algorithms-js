import heapq
from collections import defaultdict
from functools import cache
from json import dumps
from typing import List


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        N = len(grid)
        M = len(grid[0])

        data = [[0] * M for i in range(N)]
        for row in range(N):
            for col in range(M):
                if grid[row][col] == 1:
                    data[row][col] = 1

        parents = {}
        counts = {}

        def getParent(item):
            if item not in parents:
                parents[item] = item
                counts[item] = 1
                return item

            if parents[item] == item:
                return item

            parent = getParent(parents[item])
            parents[item] = parent

            return parent

        def setParent(item1, item2):
            parent1 = getParent(item1)
            parent2 = getParent(item2)
            if parent1 == parent2:
                return

            if counts[parent1] >= counts[parent2]:
                parents[parent2] = parent1
                counts[parent1] += counts[parent2]
            else:
                parents[parent1] = parent2
                counts[parent2] += counts[parent1]

        getParent((-1, -1))

        for cell in hits:
            row, col = cell
            data[row][col] = 0

        shifts = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def isValidCell(row, col):
            if row == -1 or row == N or col == -1 or col == M:
                return False
            if data[row][col] == 0:
                return False

            return True

        def connectBottom(cell):
            row, col = cell
            top = getParent((-1, -1))
            setParent((-1, -1), cell)

            for sR, sC in shifts:
                nR = row + sR
                nC = col + sC
                if not isValidCell(nR, nC):
                    continue

                parent = getParent((nR, nC))
                if parent == top:
                    continue

                connectBottom((nR, nC))

        for col in range(M):
            if data[0][col] == 0:
                continue

            setParent((-1, -1), (0, col))
            connectBottom((0, col))

        def connectNeighbor(cell):
            row, col = cell
            if row == 0:
                setParent((row, col), (-1, -1))

            for sR, sC in shifts:
                nR = row + sR
                nC = col + sC
                if not isValidCell(nR, nC):
                    continue

                parent1 = getParent((row, col))
                parent2 = getParent((nR, nC))
                if parent1 == parent2:
                    continue

                setParent((row, col), (nR, nC))
                connectNeighbor((nR, nC))

        K = len(hits)
        countConnected = [0] * (K + 1)

        for i in range(K - 1, -1, -1):
            # print(
            #     "parents",
            #     parents,
            #     "counts",
            #     counts,
            #     "top",
            #     getParent((-1, -1)),
            # )

            top = getParent((-1, -1))
            countConnected[i + 1] = counts[top] - 1

            row, col = hits[i]
            if grid[row][col] == 1:
                data[row][col] = 1
                connectNeighbor((row, col))

        top = getParent((-1, -1))
        countConnected[0] = counts[top] - 1

        # print(
        #     "countConnected",
        #     countConnected,
        # )

        res = [0] * K
        for i in range(K - 1, -1, -1):
            diff = countConnected[i] - countConnected[i + 1]
            if diff > 1:
                res[i] += diff - 1

        return res


"""
[[1], [1], [1], [1], [1]],
[[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]],
[1, 0, 1, 0, 0],

[
[1],
[1],
[1],
[0],
[0]
],
[0,0,0,0,0],


"""


def test():
    params = [
        {
            "input": [[[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]]],
            "output": [2],
        },
        {
            "input": [[[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]]],
            "output": [0, 0],
        },
        {
            "input": [
                [[1], [1], [1], [1], [1]],
                [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]],
            ],
            "output": [1, 0, 1, 0, 0],
        },
        {
            "input": [
                [[1, 1, 1], [0, 1, 0], [0, 0, 0]],
                [[0, 2], [2, 0], [0, 1], [1, 2]],
            ],
            "output": [0, 0, 1, 0],
        },
        {
            "input": [
                [[1], [1], [1], [1], [1]],
                [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]],
            ],
            "output": [1, 0, 1, 0, 0],
        },
    ]
    solution = Solution()

    for param in params:
        grid, hits = param["input"]
        result = solution.hitBricks(grid, hits)
        print(
            "SUCCESS" if result == param["output"] else "ERROR",
            "input",
            param["input"],
            "output",
            param["output"],
            "result",
            result,
            "\n",
        )


if __name__ == "__main__":
    test()
