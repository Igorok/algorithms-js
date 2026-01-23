import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math


class Solution:
    def magicalString(self, n: int) -> int:
        if n < 4:
            return 1

        memo = [1, 2, 2]
        res = 1
        id = 2

        while len(memo) < n:
            if memo[id] == 1:
                res += 1

            if memo[id] == 1:
                if memo[-1] == 1:
                    memo.append(2)
                else:
                    memo.append(1)
            else:
                if memo[-1] == 1:
                    memo = memo + [2,2]
                else:
                    memo = memo + [1,1]

            id += 1

        while id < n:
            if memo[id] == 1:
                res += 1
            id += 1

        # print('memo', memo)

        return res



def test():
    params = [
        {
            "input": 6,
            "output": 3,
        },
        {
            "input": 1,
            "output": 1
        },
        {
            "input": 11,
            "output": 5
        },
    ]
    solution = Solution()

    for param in params:
        n = param["input"]
        result = solution.magicalString(n)
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
