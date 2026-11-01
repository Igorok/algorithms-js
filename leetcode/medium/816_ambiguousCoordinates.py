import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        s = s[1 : len(s) - 1]
        N = len(s)
        prefix = [0] * N
        prefix[0] = int(s[0])
        for i in range(1, N):
            prefix[i] = prefix[i - 1] + int(s[i])

        # print(prefix)

        res = []
        for i in range(1, N):
            if i > 1 and prefix[i - 1] == 0:
                continue

            # print(i, prefix[i])

            rightSum = prefix[-1] - prefix[i - 1]
            if N - i > 1 and rightSum == 0:
                continue

            left = s[:i]
            right = s[i:]

            # print(left, right)

            for p1 in range(i):
                num1 = ""
                if p1 == 0:
                    num1 = left
                else:
                    num1 = left[:p1] + "." + left[p1:]
                    if left[p1:][-1] == "0":
                        continue

                if len(num1) > 1 and num1[0] == "0" and num1[1] != ".":
                    continue

                for p2 in range(len(right)):
                    num2 = ""
                    if p2 == 0:
                        num2 = right
                    else:
                        num2 = right[:p2] + "." + right[p2:]
                        if right[p2:][-1] == "0":
                            continue

                    if len(num2) > 1 and num2[0] == "0" and num2[1] != ".":
                        continue

                    res.append(f"({num1}, {num2})")

        return res


def test():
    params = [
        {
            "input": "(123)",
            "output": ["(1, 2.3)", "(1, 23)", "(1.2, 3)", "(12, 3)"],
        },
        {
            "input": "(0123)",
            "output": [
                "(0, 1.23)",
                "(0, 12.3)",
                "(0, 123)",
                "(0.1, 2.3)",
                "(0.1, 23)",
                "(0.12, 3)",
            ],
        },
        {
            "input": "(00011)",
            "output": ["(0, 0.011)", "(0.001, 1)"],
        },
        {
            "input": "(100)",
            "output": ["(10, 0)"],
        },
        {
            "input": "(0010)",
            "output": ["(0.01, 0)"],
        },
    ]
    solution = Solution()

    for param in params:
        s = param["input"]
        result = solution.ambiguousCoordinates(s)
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
