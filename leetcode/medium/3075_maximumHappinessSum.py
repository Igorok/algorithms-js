import json
from collections import defaultdict, deque
from typing import List
import heapq

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(key = lambda x: -x)
        res = 0
        for i in range(k):
            r = max(0, happiness[i] - i)
            if r == 0:
                break
            res += r
        return res


def test():
    params = [
        {
            "input": [[1,2,3], 2],
            "output": 4,
        },
        {
            "input": [[1,1,1,1], 2],
            "output": 1,
        },
        {
            "input": [[2,3,4,5], 1],
            "output": 5,
        },
    ]
    solution = Solution()

    for param in params:
        happiness, k = param["input"]
        result = solution.maximumHappinessSum(happiness, k)
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
