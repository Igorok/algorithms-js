import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution_0:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        N = len(s)
        M = len(queries)

        finalNum = [""] * N
        finalNum[0] = "" if s[0] == "0" else s[0]
        sumOfDigits = [0] * N
        sumOfDigits[0] = 0 if s[0] == "0" else int(s[0])

        for i in range(1, N):
            sumOfDigits[i] = sumOfDigits[i - 1] + int(s[i])

            finalNum[i] = finalNum[i - 1]
            if s[i] != "0":
                finalNum[i] = finalNum[i - 1] + s[i]

        # print(
        #     "finalNum",
        #     finalNum,
        #     "sumOfDigits",
        #     sumOfDigits,
        # )

        res = [0] * M
        for i in range(M):
            start, end = queries[i]

            # print(start, end)

            sNum = "" if start == 0 else finalNum[start - 1]
            eNum = finalNum[end]

            # print(sNum, eNum)

            num = eNum[len(sNum) :]
            num = 0 if len(num) == 0 else int(num)

            sSum = 0 if start == 0 else sumOfDigits[start - 1]
            eSum = sumOfDigits[end]
            sumOfNum = eSum - sSum

            res[i] = (num * sumOfNum) % MOD

        return res


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        N = len(s)
        M = len(queries)

        pow10 = [1] * (N + 2)
        for i in range(1, N):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        countOfDigits = [0] * N
        countOfDigits[0] = 0 if s[0] == "0" else 1

        sumOfDigits = [0] * N
        sumOfDigits[0] = 0 if s[0] == "0" else int(s[0])

        xMult = [0] * N
        xMult[0] = sumOfDigits[0]

        for i in range(1, N):
            num = int(s[i])

            if num == 0:
                xMult[i] = xMult[i - 1]
                sumOfDigits[i] = sumOfDigits[i - 1]
                countOfDigits[i] = countOfDigits[i - 1]
            else:
                xMult[i] = (xMult[i - 1] * 10 + num) % MOD
                sumOfDigits[i] = sumOfDigits[i - 1] + num
                countOfDigits[i] = countOfDigits[i - 1] + 1

        # print(
        #     "pow10",
        #     pow10,
        #     "sumOfDigits",
        #     sumOfDigits,
        #     "countOfDigits",
        #     countOfDigits,
        #     "xMult",
        #     xMult,
        # )

        res = [0] * M
        for i in range(M):
            start, end = queries[i]

            sumS = 0 if start == 0 else sumOfDigits[start - 1]
            endS = sumOfDigits[end]
            sumOfNums = endS - sumS

            xS = 0 if start == 0 else xMult[start - 1]
            xE = xMult[end]

            cntS = 0 if start == 0 else countOfDigits[start - 1]
            cntE = countOfDigits[end]

            cntDigits = cntE - cntS

            # print("cntDigits", cntDigits)

            xS = xS * pow10[cntDigits]
            x = (MOD + xE - xS) % MOD

            res[i] = (x * sumOfNums) % MOD

        return res


def test():
    params = [
        # {
        #     "input": ["10203004", [[0, 7], [1, 3], [4, 6]]],
        #     "output": [12340, 4, 9],
        # },
        # {
        #     "input": ["1000", [[0, 3], [1, 1]]],
        #     "output": [1, 0],
        # },
        # {
        #     "input": ["9876543210", [[0, 9]]],
        #     "output": [444444137],
        # },
        {
            "input": ["3", [[0, 0]]],
            "output": [0],
        },
    ]
    solution = Solution()

    for param in params:
        s, queries = param["input"]
        result = solution.sumAndMultiply(s, queries)

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
