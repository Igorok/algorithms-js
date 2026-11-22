import heapq
import json
from collections import Counter, defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        def getNum(word):
            char = 'z'
            cnt = 0

            for c in word:
                if c < char:
                    char = c
                    cnt = 1
                    continue

                if c == char:
                    cnt += 1

            return cnt

        wArr = [getNum(w) for w in words]
        wArr.sort()
        N = len(wArr)

        def getCnt(word):
            num = getNum(word)

            start = 0
            end = N - 1
            id = -1

            while start <= end:
                m = (start + end) // 2
                if wArr[m] > num:
                    id = m
                    end = m - 1
                else:
                    start = m + 1

            return 0 if id == -1 else N - id


        res = [getCnt(w) for w in queries]


        return res


def test():
    params = [
        {
            "input": [["cbd"], ["zaaaz"]],
            "output": [1],
        },
        {
            "input": [["bbb", "cc"], ["a", "aa", "aaa", "aaaa"]],
            "output": [1, 2],
        },
    ]
    solution = Solution()

    for param in params:
        queries, words = param["input"]
        result = solution.numSmallerByFrequency(queries, words)

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
