import json
import math
from collections import Counter, defaultdict, deque

# from functools import cache
from linecache import cache
from typing import List


class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set(["a", "e", "i", "o", "u"])

        N = len(word)
        res = 0
        for i in range(N):
            if word[i] not in vowels:
                continue

            ends = N - i
            starts = i + 1
            res += ends * starts

        return res


def test():
    params = [
        {"input": "aba", "output": 6},
        {"input": "abc", "output": 3},
        {"input": "ltcd", "output": 0},
    ]
    solution = Solution()

    for param in params:
        word = param["input"]
        result = solution.countVowels(word)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            # msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
