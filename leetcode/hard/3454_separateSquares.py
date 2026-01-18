import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        return 0





def test():
    params = [
        {
            "input": [[0,0,1],[2,2,1]],
            "output": 1.00000,
        },
        {
            "input": [[0,0,2],[1,1,1]],
            "output": 1.00000,
        },
    ]
    solution = Solution()

    for param in params:
        squares = param["input"]
        result = solution.separateSquares(squares)
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
