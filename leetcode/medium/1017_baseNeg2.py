import math
from collections import deque
from functools import cache
from json import dumps
from typing import List


class Solution:
    def baseNeg2(self, n: int) -> str:
        div = -2
        res = []

        while n != 0:
            rem = n % div
            n = n // div

            if rem < 0:
                rem += 2
                # rem + 2 + num - 2 = rem + (degree + 1) * -2
                n += 1
            res.append(str(abs(rem)))

        res.reverse()

        return "".join(res)


def test():
    params = [
        {
            "input": 2,
            "output": "110",
        },
        {
            "input": 3,
            "output": "111",
        },
        {
            "input": 4,
            "output": "100",
        },
        {
            "input": 10,
            "output": "11110",
        },
    ]
    solution = Solution()

    for param in params:
        n = param["input"]
        result = solution.baseNeg2(n)
        print(
            "SUCCESS" if result == param["output"] else "ERROR",
            "input",
            param["input"],
            "output",
            param["output"],
            "result",
            result,
            "\n",
        )


if __name__ == "__main__":
    test()
