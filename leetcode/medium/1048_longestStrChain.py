import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math
import heapq

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordsByLength = defaultdict(list)
        prevCount = {}

        for word in words:
            wordsByLength[len(word)].append(word)
            if word in prevCount:
                continue
            prevCount[word] = 1

        wordsByLength = dict(sorted(wordsByLength.items()))
        res = 1

        for length in wordsByLength:
            if length == 1:
                continue
            if length-1 not in wordsByLength:
                continue

            for curr in wordsByLength[length]:
                for prev in wordsByLength[length-1]:
                    id1 = 0
                    id2 = 0

                    while id1 < length-1 and id2 < length:
                        if prev[id1] == curr[id2]:
                            id1 += 1
                            id2 += 1
                        else:
                            id2 += 1

                    if id1 == length-1:
                        prevCount[curr] = max(prevCount[curr], prevCount[prev] + 1)
                        res = max(res, prevCount[curr])


        return res

def test():
    params = [
        {
            "input": ["a","b","ba","bca","bda","bdca"],
            "output": 4,
        },
        {
            "input": ["xbc","pcxbcf","xb","cxbc","pcxbc"],
            "output": 5,
        },
        {
            "input": ["abcd","dbqca"],
            "output": 1,
        },
    ]
    solution = Solution()

    for param in params:
        words = param["input"]
        result = solution.longestStrChain(words)
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
