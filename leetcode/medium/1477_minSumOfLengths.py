import json
from collections import deque
from functools import cache
from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        N = len(arr)
        left = 0
        data = []
        acc = 0

        for right in range(N):
            acc += arr[right]

            while acc >= target:
                if acc == target:
                    if len(data) == 0 or data[-1][1] != right:
                        data.append([left, right])
                    else:
                        data[-1][0] = left

                acc -= arr[left]
                left += 1

        # print("data", data)

        dataLen = len(data)
        if dataLen < 2:
            return -1

        lengthByStart = [None] * dataLen
        lengthByStart[dataLen - 1] = [
            data[dataLen - 1][0],
            data[dataLen - 1][1] - data[dataLen - 1][0] + 1,
        ]
        for i in range(dataLen - 2, -1, -1):
            lengthByStart[i] = [
                data[i][0],
                min(lengthByStart[i + 1][1], data[i][1] - data[i][0] + 1),
            ]

        # print("lengthByStart", lengthByStart)

        res = -1
        point = 1
        for start, end in data:
            while point < dataLen and lengthByStart[point][0] <= end:
                point += 1

            if point == dataLen:
                break

            curr = end - start + 1
            right = lengthByStart[point][1]

            if res == -1:
                res = curr + right
                continue

            res = min(res, curr + right)

        return res


def test():
    params = [
        {
            "input": [[3, 2, 2, 4, 3], 3],
            "output": 2,
        },
        {
            "input": [[7, 3, 4, 7], 7],
            "output": 2,
        },
        {
            "input": [[4, 3, 2, 6, 2, 3, 4], 6],
            "output": -1,
        },
        {
            "input": [[0, 0, 0, 0, 1, 1], 1],
            "output": 2,
        },
        {
            "input": [[5, 5, 4, 4, 5], 3],
            "output": -1,
        },
    ]
    solution = Solution()

    for param in params:
        arr, target = param["input"]
        result = solution.minSumOfLengths(arr, target)
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
