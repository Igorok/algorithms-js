import sys

sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        text = []
        N = len(s)
        left = 0
        for right in range(N):
            if s[right] != s[left]:
                text.append([s[left], right - left])
                left = right
        text.append([s[left], N - left])

        # print("text", text)

        def check(arr):
            id = len(arr) - 1
            char = arr[id][0]
            cnt = arr[id][1]
            if id >= len(text) or char != text[id][0]:
                return False

            if cnt != text[id][1] and (text[id][1] < 3 or text[id][1] < cnt):
                return False

            return True

        res = 0
        for word in words:
            M = len(word)
            correct = True

            arr = []
            left = 0
            for right in range(M):
                if word[right] != word[left]:
                    arr.append([word[left], right - left])
                    left = right

                    correct = check(arr)
                    if not correct:
                        break

            arr.append([word[left], M - left])
            if correct:
                correct = check(arr) and len(text) == len(arr)

            # print('arr', arr, correct)

            if correct:
                res += 1

        return res


def test():
    params = [
        # {
        #     "input": ["heeellooo", ["hello", "hi", "helo"]],
        #     "output": 1,
        # },
        # {
        #     "input": ["zzzzzyyyyy", ["zzyy", "zy", "zyy"]],
        #     "output": 3,
        # },
        # {
        #     "input": ["lll", ["ll"]],
        #     "output": 1,
        # },
        # {
        #     "input": ["abcd", ["abc"]],
        #     "output": 0,
        # },
        {
            "input": ["dddiiiinnssssssoooo", ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]],
            "output": 3,
        },
    ]
    solution = Solution()

    for param in params:
        s, words = param["input"]
        result = solution.expressiveWords(s, words)
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
