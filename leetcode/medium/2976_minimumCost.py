import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math
import heapq

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = {}
        for i in range(len(original)):
            adj[original[i]] = adj.get(original[i], {})
            price = adj[original[i]].get(changed[i], float('inf'))
            adj[original[i]][changed[i]] = min(price, cost[i])

        def find(start, end):
            if start == end:
                return 0

            nodesQueue = [(0, start)]
            visited = {}
            visited[start] = 0

            while nodesQueue:
                weight, node = heapq.heappop(nodesQueue)

                if weight > visited[node]:
                    continue

                if node == end:
                    return weight

                neighbors = adj.get(node, {})
                for nei, w in neighbors.items():
                    if nei not in visited or visited[nei] > w + weight:
                        visited[nei] = w+weight
                        heapq.heappush(nodesQueue, (w+weight, nei))


            return -1

        res = 0
        for i in range(len(source)):
            r = find(source[i], target[i])
            if r == -1:
                return -1
            else:
                res += r


        return res


def test():
    params = [
        {
            "input": ["abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]],
            "output": 28,
        },
        {
            "input": ["aaaa", "bbbb", ["a","c"], ["c","b"], [1,2]],
            "output": 12,
        },
        {
            "input": ["abcd", "abce", ["a"], ["e"], [10000]],
            "output": -1,
        },
    ]
    solution = Solution()

    for param in params:
        source, target, original, changed, cost = param["input"]
        result = solution.minimumCost(source, target, original, changed, cost)
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
