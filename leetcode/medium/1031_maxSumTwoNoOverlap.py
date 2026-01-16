import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        N = len(nums)

        prefixSum = [0]*N
        prefixSum[0] = nums[0]
        for i in range(1, N):
            prefixSum[i] = prefixSum[i-1] + nums[i]

        rightMaxSum = [[0]*N for i in range(2)]
        for i in range(N-1, -1, -1):
            left = 0 if i == 0 else prefixSum[i-1]

            if i <= N-firstLen:
                prev = rightMaxSum[0][i+1] if i+1 < N else 0
                s = prefixSum[i + firstLen - 1] - prefixSum[i-1]
                rightMaxSum[0][i] = max(prev, s)

            if i <= N-secondLen:
                prev = rightMaxSum[1][i+1] if i+1 < N else 0
                s = prefixSum[i + secondLen - 1] - prefixSum[i-1]
                rightMaxSum[1][i] = max(prev, s)


        res = 0

        for i in range(N):
            left = 0 if i == 0 else prefixSum[i-1]

            if i + firstLen + secondLen > N:
                break

            rId = i + firstLen
            s = prefixSum[rId - 1] - left
            maxRight = rightMaxSum[1][rId]

            res = max(res, s + maxRight)

            rId = i + secondLen
            s = prefixSum[rId - 1] - left
            maxRight = rightMaxSum[0][rId]

            res = max(res, s + maxRight)

        return res


def test():
    params = [
        {
            "input": [[0,6,5,2,2,5,1,9,4], 1, 2],
            "output": 20,
        },
        {
            "input": [[3,8,1,3,2,1,8,9,0], 3, 2],
            "output": 29,
        },
        {
            "input": [[2,1,5,6,0,9,5,0,3,8], 4, 3],
            "output": 31,
        },
        {
            "input": [[1,0,1],1,1],
            "output": 2,
        },
    ]
    solution = Solution()

    for param in params:
        nums, firstLen, secondLen = param["input"]
        result = solution.maxSumTwoNoOverlap(nums, firstLen, secondLen)
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
