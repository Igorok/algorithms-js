import heapq
import json
from collections import deque
from typing import List


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        if num2 < 100:
            return 0

        res = 0

        for num in range(max(num1, 100), num2 + 1):
            word = str(num)
            for i in range(1, len(word) - 1):
                if word[i - 1] < word[i] and word[i + 1] < word[i]:
                    res += 1
                if word[i] < word[i - 1] and word[i] < word[i + 1]:
                    res += 1

        return res


def test():
    params = [
        {
            "input": [120, 130],
            "output": 3,
        },
        {
            "input": [198, 202],
            "output": 3,
        },
        {
            "input": [4848, 4848],
            "output": 2,
        },
    ]

    solution = Solution()

    for param in params:
        num1, num2 = param["input"]
        result = solution.totalWaviness(num1, num2)
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
