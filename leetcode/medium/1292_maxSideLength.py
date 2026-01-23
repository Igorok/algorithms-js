import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        N = len(mat)
        M = len(mat[0])

        res = 0
        memo = [[0]*M for i in range(N)]

        for row in range(N):
            for col in range(M):
                top = 0 if row == 0 else memo[row-1][col]
                left = 0 if col == 0 else memo[row][col-1]
                diag = 0 if top == 0 or col == 0 else memo[row-1][col-1]

                memo[row][col] = mat[row][col] + top + left - diag


                start = 1
                end = min(col, row) + 1
                while start <= end:
                    length = (start + end) // 2

                    _top = 0 if row - length < 0 else memo[row-length][col]
                    _left = 0 if col - length < 0 else memo[row][col-length]
                    _diag = 0 if row - length < 0 or col - length < 0 else memo[row-length][col-length]
                    val = memo[row][col] - _top - _left + _diag

                    if val <= threshold:
                        res = max(res, length)
                        start = length + 1
                    else:
                        end = length - 1

        return res


def test():
    params = [
        {
            "input": [[[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4],
            "output": 2,
        },
        {
            "input": [
                [
                    [2,2,2,2,2],
                    [2,2,2,2,2],
                    [2,2,2,2,2],
                    [2,2,2,2,2],
                    [2,2,2,2,2]
            ], 1],
            "output": 0
        },
    ]
    solution = Solution()

    for param in params:
        mat, threshold = param["input"]
        result = solution.maxSideLength(mat, threshold)
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
