import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        hightStr = str(high)
        lowStr = str(low)

        res = []

        for i in range(len(lowStr), len(hightStr) + 1):
            start = 1 if i > len(lowStr) else int(lowStr[0])

            for curr in range(start, 10):
                num = curr
                for j in range(1, i):
                    rem = (curr + j) % 10

                    if rem <= num % 10:
                        break
                    num *= 10
                    num += rem

                if num > high:
                    break

                if num >= low and num <= high and len(str(num)) == i:
                    res.append(num)

        return res


def test():
    params = [
        {
            "input": [100, 300],
            "output": [123, 234],
        },
        {
            "input": [1000, 13000],
            "output": [1234, 2345, 3456, 4567, 5678, 6789, 12345],
        },
    ]
    solution = Solution()

    for param in params:
        low, high = param["input"]
        result = solution.sequentialDigits(low, high)

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
