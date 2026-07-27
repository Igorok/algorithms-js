import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        res = ""

        def isValid(text):
            if int(text[:2]) > 23:
                return False

            if int(text[3:]) > 59:
                return False

            return True

        def isGreat(text1, text2):
            if text1 == "":
                return True

            for i in range(5):
                if i == 2:
                    continue
                if text2[i] == text1[i]:
                    continue
                if text2[i] > text1[i]:
                    return True
                else:
                    return False

            return False

        def rec(id, acc, visited):
            nonlocal res
            if id == 4:
                # print(1, acc)
                if isValid(acc) and isGreat(res, acc):
                    res = acc
                    # print(2, res)
                return

            for i in range(4):
                if id == 0 and arr[i] > 2:
                    continue
                if id == 2 and arr[i] > 5:
                    continue

                bit = visited >> i
                if (bit & 1) == 1:
                    continue
                newId = id + 1
                newText = acc + str(arr[i])
                if id == 1:
                    newText += ":"
                newVisited = visited | (1 << i)

                rec(newId, newText, newVisited)

        rec(0, "", 0)
        return res


def test():
    params = [
        {
            "input": [1, 2, 3, 4],
            "output": "23:41",
        },
        {
            "input": [5, 5, 5, 5],
            "output": "",
        },
        {
            "input": [0, 0, 1, 0],
            "output": "10:00",
        },
    ]
    solution = Solution()

    for param in params:
        arr = param["input"]
        result = solution.largestTimeFromDigits(arr)

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
