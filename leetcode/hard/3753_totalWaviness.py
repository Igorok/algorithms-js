import heapq
import json
from collections import deque
from functools import cache
from typing import List

"""
Do you know leetcode issue "3753. Total Waviness of Numbers in Range II"?
In previous issue I just iterate all nums from start to end. But it is impossible for 10^15.

So it looks I take a start like a string and iterate to the end like a string in recursion. Every time I should make a wave like a "10"+[1-9]. Something like that.

"""


class Solution:
    def _isWave(self, num1, num2, num3):
        if num1 == -1 or num2 == -1:
            return False

        if num1 > num2 and num3 > num2:
            return True

        if num1 < num2 and num3 < num2:
            return True

        return False

    def _getWaviness(self, num: int) -> int:
        if num < 100:
            return 0

        arr = []

        while num > 0:
            arr.append(num % 10)
            num = num // 10

        arr.reverse()

        @cache
        def rec(id, prev1, prev2, isLess, isZero):
            if id == len(arr):
                return (1, 0)

            countOfNums = 0
            countOfWaves = 0

            for num in range(10):
                if isLess == 0 and num > arr[id]:
                    break

                nextIsLess = 1
                if isLess == 0 and num == arr[id]:
                    nextIsLess = 0

                nextIsZero = 1 if isZero == 1 and num == 0 else 0
                currVal = num
                if nextIsZero == 1:
                    currVal = -1

                cntNum, cntWave = rec(id + 1, prev2, currVal, nextIsLess, nextIsZero)
                countOfNums += cntNum
                countOfWaves += cntWave
                if self._isWave(prev1, prev2, num):
                    countOfWaves += cntNum

            return (countOfNums, countOfWaves)

        return rec(0, -1, -1, 0, 1)[1]

    def totalWaviness(self, num1: int, num2: int) -> int:
        res1 = self._getWaviness(num1 - 1)
        res2 = self._getWaviness(num2)

        return res2 - res1


def test():
    params = [
        {
            "input": [11101, 11101],
            "output": 1,
        },
        {
            "input": [1201, 1201],
            "output": 2,
        },
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
