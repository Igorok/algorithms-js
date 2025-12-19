import json
from collections import defaultdict, deque
from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:


        return 0


def test():
    params = [
        {
            "input": [prices = [1,7,9,8,2], k = 2],
            "output": 5,
        },
    ]
    solution = Solution()

    for param in params:
        n, present, future, hierarchy, budget = param["input"]
        result = solution.maxProfit(n, present, future, hierarchy, budget)
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
