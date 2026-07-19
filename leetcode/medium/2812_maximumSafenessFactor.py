import heapq
import json
import math
from collections import defaultdict, deque
from typing import List


class Solution_0:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return 0
        if grid[-1][-1] == 1:
            return 0

        shifts = ((1, 0), (-1, 0), (0, 1), (0, -1))

        N = len(grid)
        zeros = []
        ones = []

        memo = [[N] * N for i in range(N)]

        for row in range(N):
            for col in range(N):
                if grid[row][col] == 0:
                    zeros.append([row, col])
                else:
                    ones.append([row, col])
                    memo[row][col] = 0

        # print("zeros", zeros)
        # print("ones", ones)

        for zero in zeros:
            for one in ones:
                dist = abs(one[0] - zero[0]) + abs(one[1] - zero[1])
                memo[zero[0]][zero[1]] = min(memo[zero[0]][zero[1]], dist)

        # print("memo", memo)

        cellQueue = [(-memo[0][0], 0, 0)]
        visited = [[0] * N for i in range(N)]
        visited[0][0] = 1

        while cellQueue:
            d, r, c = heapq.heappop(cellQueue)
            d = -d

            if r == N - 1 and c == N - 1:
                return d

            for sR, sC in shifts:
                newR = r + sR
                newC = c + sC

                if newR < 0 or newR >= N or newC < 0 or newC >= N:
                    continue

                if grid[newR][newC] == 1 or visited[newR][newC] == 1:
                    continue

                dist = min(memo[newR][newC], d)
                visited[newR][newC] = 1

                heapq.heappush(cellQueue, (-dist, newR, newC))

        return 0


class Solution:
    def _getDistTable(self):
        memo = [[self.N + 1] * self.N for i in range(self.N)]

        onesQueue = deque()

        for row in range(self.N):
            for col in range(self.N):
                if self.grid[row][col] == 1:
                    memo[row][col] = 0
                    onesQueue.append((0, row, col))

        while onesQueue:
            dist, row, col = onesQueue.popleft()

            for sR, sC in self.shifts:
                newR = sR + row
                newC = sC + col

                if newR < 0 or newR == self.N or newC < 0 or newC == self.N:
                    continue

                # Manhattan distance = abs(r1 - r2) + (c1 - c2)
                # every step we can add only +1 to dist, from row or column
                # so location is not important
                if self.grid[newR][newC] == 1 or memo[newR][newC] <= dist + 1:
                    continue

                memo[newR][newC] = dist + 1
                onesQueue.append((dist + 1, newR, newC))

        return memo

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return 0
        if grid[-1][-1] == 1:
            return 0

        self.shifts = ((1, 0), (-1, 0), (0, 1), (0, -1))
        self.grid = grid
        self.N = len(grid)

        memo = self._getDistTable()

        # print("memo", memo)

        cellQueue = [(-memo[0][0], 0, 0)]
        visited = [[0] * self.N for i in range(self.N)]
        visited[0][0] = 1

        while cellQueue:
            d, r, c = heapq.heappop(cellQueue)
            d = -d

            if r == self.N - 1 and c == self.N - 1:
                return d

            for sR, sC in self.shifts:
                newR = r + sR
                newC = c + sC

                if newR < 0 or newR >= self.N or newC < 0 or newC >= self.N:
                    continue

                if grid[newR][newC] == 1 or visited[newR][newC] == 1:
                    continue

                dist = min(memo[newR][newC], d)
                visited[newR][newC] = 1

                heapq.heappush(cellQueue, (-dist, newR, newC))

        return 0


def test():
    params = [
        {
            "input": [[1, 0, 0], [0, 0, 0], [0, 0, 1]],
            "output": 0,
        },
        {
            "input": [[0, 0, 1], [0, 0, 0], [0, 0, 0]],
            "output": 2,
        },
        {
            "input": [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]],
            "output": 2,
        },
    ]
    solution = Solution()

    for param in params:
        s = param["input"]
        result = solution.maximumSafenessFactor(s)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
