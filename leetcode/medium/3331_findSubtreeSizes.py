import heapq
import json
from collections import Counter, defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        N = len(parent)

        def getAdj():
            adj = [[] for i in range(N)]
            for i in range(1, N):
                p = parent[i]
                adj[p].append(i)
            return adj

        adj = getAdj()

        def changeParent(node, _chars):
            char = s[node]
            chars = _chars.copy()

            if char in chars:
                parent[node] = chars[char]
            chars[char] = node

            for child in adj[node]:
                changeParent(child, chars)

            del chars

        changeParent(0, {})

        adj = getAdj()
        countOfNodes = [-1]*N

        def calculate(node):
            countOfNodes[node] = 1
            for child in adj[node]:
                countOfNodes[node] += calculate(child)
            return countOfNodes[node]

        for i in range(N):
            if countOfNodes[i] != -1:
                continue
            countOfNodes[i] = calculate(i)

        return countOfNodes


def test():
    params = [
        {
            "input": [[-1,0,0,1,1,1], "abaabc"],
            "output": [6,3,1,1,1,1],
        },
        {
            "input": [[-1,0,4,0,1], "abbba"],
            "output":[5,2,1,1,1],
        },
    ]
    solution = Solution()

    for param in params:
        parent, s = param["input"]
        result = solution.findSubtreeSizes(parent, s)

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
