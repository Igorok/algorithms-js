import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List

class Solution_0:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        @cache
        def getPrice(id):
            if id == n-1:
                return 0

            cost = float('inf')

            for i in range(1, 4):
                if id+i >= n:
                    break
                c = costs[id+i] + i**2
                c += getPrice(id + i)

                cost = min(cost, c)

            return cost


        return getPrice(-1)


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        res = [float('inf')]*n

        for id in range(n):
            for diff in range(1, 4):
                prev = 0 if id - diff < 0 else res[id-diff]
                res[id] = min(res[id], costs[id] + prev + diff**2)

        return res[-1]

def test():
    params = [
        {
            "input": [4, [1,2,3,4]],
            "output": 13,
        },
        {
            "input": [4, [5,1,6,2]],
            "output": 11,
        },
        {
            "input": [3, [9,8,3]],
            "output": 12,
        },
    ]
    solution = Solution()

    for param in params:
        n, costs = param["input"]
        result = solution.climbStairs(n, costs)
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
