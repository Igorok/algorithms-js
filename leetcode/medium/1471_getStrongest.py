import heapq
import json
from collections import deque
from functools import cache
from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        N = len(arr)
        data = [(arr[i], i) for i in range(N)]
        data.sort()
        middle = (N - 1) // 2
        res = []

        print(data)
        print("middle", data[middle][0])

        start = middle
        end = middle + 1

        while start > -1 and end < N:
            diffStart = abs(data[start][0] - data[middle][0])
            diffEnd = abs(data[end][0] - data[middle][0])

            if diffStart == diffEnd:
                if data[start][0] < data[end][0]:
                    res.append(data[start][0])
                    start -= 1
                else:
                    res.append(data[end][0])
                    end += 1
            elif diffStart < diffEnd:
                res.append(data[start][0])
                start -= 1
            else:
                res.append(data[end][0])
                end += 1

        while start > -1:
            res.append(data[start][0])
            start -= 1

        while end < N:
            res.append(data[end][0])
            end += 1

        print(res)

        return res[(N - k) :]


"""

[(-9, 4), (-8, 3), (-7, 5), (-6, 2), (-5, 6), (-4, 1), (-3, 7), (-2, 0), (-1, 8)]
middle -5
[-5, -4, -6, -7, -3, -2, -8, -9, -1]


[(-9, 4), (-8, 3), (-7, 5), (-6, 2), (-5, 6), (-4, 1), (-3, 7), (-2, 0), (-1, 8)]
-5 6
-4 1
-6 2
-7 5
-3 7
-2 0
-8 3
-9 4
-1 8

Do you know this leetcode issue "1471. The k Strongest Values in an Array"?
[-2, -4, -6, -8, -9, -7, -5, -3, -1], 3
why answer is [-1, -9, -2], not a [-8, -9, -1]?

"""


def test():
    params = [
        # {
        #     "input": [[1, 2, 3, 4, 5], 2],
        #     "output": [5, 1],
        # },
        # {
        #     "input": [[1, 1, 3, 5, 5], 2],
        #     "output": [5, 5],
        # },
        # {
        #     "input": [[6, 7, 11, 7, 6, 8], 5],
        #     "output": [11, 8, 6, 6, 7],
        # },
        {
            "input": [[-2, -4, -6, -8, -9, -7, -5, -3, -1], 3],
            "output": [-1, -9, -2],
        },
    ]

    solution = Solution()

    for param in params:
        arr, k = param["input"]
        result = solution.getStrongest(arr, k)
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
