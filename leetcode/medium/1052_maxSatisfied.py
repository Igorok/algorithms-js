import heapq
import json
from collections import deque
from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        n = len(customers)

        curr = 0
        for i in range(n):
            if grumpy[i] == 0:
                curr += customers[i]

        for i in range(minutes):
            if grumpy[i] == 1:
                curr += customers[i]

        res = curr

        for i in range(1, n - minutes + 1):
            oldId = i - 1
            if grumpy[oldId] == 1:
                curr -= customers[oldId]

            newId = i + minutes - 1
            if grumpy[newId] == 1:
                curr += customers[newId]

            res = max(res, curr)

        return res


"""
 0  1  2  3  4  5  6  7
[1, 0, 1, 2, 1, 1, 7, 5],
[0, 1, 0, 1, 0, 1, 0, 1], 3
1+1+1+1+7+5

"""


def test():
    params = [
        {
            "input": [[1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3],
            "output": 16,
        },
        {
            "input": [[1], [0], 1],
            "output": 1,
        },
    ]

    solution = Solution()

    for param in params:
        customers, grumpy, minutes = param["input"]
        result = solution.maxSatisfied(customers, grumpy, minutes)
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
