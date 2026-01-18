import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math

class Solution_0:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        def dfs(point, id, acc):
            nonlocal N, points

            if id == N:
                return acc

            x1, y1 = point
            x2, y2 = points[id]

            hor = abs(x1-x2)
            vert = abs(y1-y2)

            if hor == 0 and vert == 0:
                return dfs(points[id], id+1, acc)

            if hor == 0 or vert == 0:
                return dfs(points[id], id+1, acc + max(hor, vert))

            if hor == vert:
                return dfs(points[id], id+1, acc+hor)

            # diagonal step
            # min(hor, vert) = diagonal step
            # max(hor, vert) - diagonal = step to arrive to diagonal point
            # path = max(hor, vert)


            return dfs(points[id], id+1, acc+max(hor, vert))


        return dfs(points[0], 1, 0)

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        res = 0

        for i in range(1, N):
            x1, y1 = points[i-1]
            x2, y2 = points[i]

            hor = abs(x1-x2)
            ver = abs(y1-y2)

            res += max(hor, ver)

        return res

def test():
    params = [
        {
            "input": [[1,1],[3,4],[-1,0]],
            "output": 7,
        },
        {
            "input": [[3,2],[-2,2]],
            "output": 5,
        },
    ]
    solution = Solution()

    for param in params:
        points = param["input"]
        result = solution.minTimeToVisitAllPoints(points)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            # msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
