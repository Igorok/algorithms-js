import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    def minimumRemoval(self, beans: list[int]) -> int:
        N = len(beans)
        if N == 1:
            return 0

        beans.sort()
        prefixSum = [0] * N
        prefixSum[0] = beans[0]
        for i in range(1, N):
            prefixSum[i] = beans[i] + prefixSum[i - 1]

        res = float("inf")
        for i in range(N):
            zeroSum = 0 if i == 0 else prefixSum[i - 1]
            rightSum = prefixSum[-1] - prefixSum[i]
            wantSum = (N - i - 1) * beans[i]
            op = rightSum - wantSum

            res = min(res, op + zeroSum)

        return res



def test():
    params = [
        {
            "input": [4, 1, 6, 5],
            "output": 4,
        },
        {
            "input": [2, 10, 3, 2],
            "output": 7,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.minimumRemoval(nums)
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
