import json
from collections import deque
from functools import cache
from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers = [0] * 10

        for d in digits:
            numbers[d] += 1

        res = set()

        def rec(id, nums):
            nonlocal numbers, res

            if id == 3:
                res.add("".join(nums))
                return

            for i in range(10):
                if numbers[i] == 0:
                    continue

                if id == 2 and i == 0:
                    continue

                if id == 0 and (i % 2) == 1:
                    continue

                nums.append(str(i))
                numbers[i] -= 1

                rec(id + 1, nums)

                nums.pop()
                numbers[i] += 1

        rec(0, [])

        return len(res)


def test():
    params = [
        {
            "input": [1, 2, 3, 4],
            "output": 12,
        },
        {
            "input": [0, 2, 2],
            "output": 2,
        },
        {
            "input": [6, 6, 6],
            "output": 1,
        },
        {
            "input": [1, 3, 5],
            "output": 0,
        },
    ]
    solution = Solution()

    for param in params:
        digits = param["input"]
        result = solution.totalNumbers(digits)
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
