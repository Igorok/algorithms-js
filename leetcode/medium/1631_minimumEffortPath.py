from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        shifts = ((1,0), (-1,0), (0,1), (0,-1))
        N = len(heights)
        M = len(heights[0])
        memo = [[float('inf')]*M for i in range(N)]
        memo[0][0] = 0

        cellQueue = [(0, 0, 0)]

        while cellQueue:
            e, r, c = heapq.heappop(cellQueue)

            if r == N-1 and c == M-1:
                continue

            for sR, sC in shifts:
                newR = r + sR
                newC = c + sC

                if newR < 0 or newR == N or newC < 0 or newC == M:
                    continue

                eff = max(e, abs(heights[newR][newC] - heights[r][c]))

                if eff < memo[newR][newC]:
                    memo[newR][newC] = eff
                    heapq.heappush(cellQueue, (eff, newR, newC))


        return memo[-1][-1]

def test ():
    params = [
        {
            'input': [[1,2,2],[3,8,2],[5,3,5]],
            'output': 2,
        },
        {
            'input': [[1,2,3],[3,8,4],[5,3,5]],
            'output': 1,
        },
        {
            'input': [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minimumEffortPath(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
