from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        return 0


def test():
    params = [
        {
            "input": [5, 5, [1,10,100,10000,1000000]],
            "output": 991600007,
        },
        {
            "input": [2, 2, [5,4,3,2,1]],
            "output": 170,
        },
        {
            "input": [1, 1, [28]],
            "output": 28,
        },
    ]
    solution = Solution()

    for param in params:
        m, k, nums = param["input"]
        result = solution.magicalSum(m, k, nums)
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
