import heapq
import json
from collections import deque
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        N = len(target)
        finalString = "-" * N

        avaliable = [0] * 26
        required = [0] * 26
        charsByStickers = {}

        for word in stickers:
            if word in charsByStickers:
                continue
            charsByStickers[word] = [0] * 26

            for char in word:
                id = ord(char) - ord("a")
                avaliable[id] += 1
                charsByStickers[word][id] += 1

        for char in target:
            id = ord(char) - ord("a")
            required[id] += 1
            if required[id] > 0 and avaliable[id] == 0:
                return -1

        visited = set()
        memo = {}

        def rec(word):
            if word == finalString:
                return 0

            if word in memo:
                return memo[word]

            if word in visited:
                return float("inf")

            visited.add(word)

            res = float("inf")
            for sticker in charsByStickers:
                curr = list(word)
                count = charsByStickers[sticker].copy()
                for i in range(len(curr)):
                    if curr[i] == "-":
                        continue
                    id = ord(curr[i]) - ord("a")
                    if count[id] == 0:
                        continue
                    curr[i] = "-"
                    count[id] -= 1

                currStr = "".join(curr)
                r = 1 + rec(currStr)
                res = min(res, r)

            memo[word] = res
            return res

        return rec(target)


def test():
    params = [
        {
            "input": [["with", "example", "science"], "thehat"],
            "output": 3,
        },
        {
            "input": [["notice", "possible"], "basicbasic"],
            "output": -1,
        },
    ]

    solution = Solution()

    for param in params:
        stickers, target = param["input"]
        result = solution.minStickers(stickers, target)
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
