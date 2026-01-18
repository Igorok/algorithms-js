import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math

# 1 <= n <= 30
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N = len(img1)
        M = len(img1[0])
        res = 0

        for shiftR in range(-N, N):
            for shiftC in range(-M, M):
                r = 0
                for row in range(N):
                    newR = row + shiftR
                    if newR < 0 or newR >= N:
                        continue
                    for col in range(M):
                        newC = col + shiftC
                        if newC < 0 or newC >= M:
                            continue

                        if img1[row][col] == 1 and img2[newR][newC] == 1:
                            r += 1

                res = max(res, r)


        return res

def test():
    params = [
        {
            "input": [[[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]],
            "output": 3,
        },
        {
            "input": [[[1]], [[1]]],
            "output": 1,
        },
        {
            "input": [[[0]], [[0]]],
            "output": 0,
        },
        {
            "input": [[[0]], [[1]]],
            "output": 0,
        },
    ]
    solution = Solution()

    for param in params:
        img1, img2 = param["input"]
        result = solution.largestOverlap(img1, img2)
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
