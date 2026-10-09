import json
from collections import deque
from functools import cache
from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        N = len(position)
        position.sort()

        def isOk(minDist):
            prev = position[0]
            cnt = m - 1

            for i in range(1, N):
                if position[i] - prev < minDist:
                    continue
                prev = position[i]
                cnt -= 1
                if cnt == 0:
                    return True

            return cnt == 0

        start = 0
        end = (position[-1] - position[0]) // (m - 1)
        res = 0

        while start <= end:
            middle = (start + end) // 2

            if isOk(middle):
                res = middle
                start = middle + 1
            else:
                end = middle - 1

        return res


def test():
    params = [
        {
            "input": [[1, 2, 3, 4, 7], 3],
            "output": 3,
        },
        {
            "input": [[5, 4, 3, 2, 1, 1000000000], 2],
            "output": 999999999,
        },
    ]
    solution = Solution()

    for param in params:
        position, m = param["input"]
        result = solution.maxDistance(position, m)
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
