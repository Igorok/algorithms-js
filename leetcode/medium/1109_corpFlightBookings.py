import json
from collections import deque
from functools import cache
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        memo = [0] * n

        for start, end, val in bookings:
            memo[start - 1] += val
            if end < n:
                memo[end] -= val

        res = [0] * n
        res[0] = memo[0]
        for i in range(1, n):
            res[i] = memo[i] + res[i - 1]

        return res


def test():
    params = [
        {
            "input": [[[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5],
            "output": [10, 55, 45, 25, 25],
        },
        {
            "input": [[[1, 2, 10], [2, 2, 15]], 2],
            "output": [10, 25],
        },
    ]
    solution = Solution()

    for param in params:
        bookings, n = param["input"]
        result = solution.corpFlightBookings(bookings, n)
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
