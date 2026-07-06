import heapq
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from typing import List

class DSU:
    def __init__(self, n):
        self.scores = [float('inf')] * n
        self.parents = [i for i in range(n)]
        self.count = [1]*n

    def getParent(self, node):
        if node == self.parents[node]:
            return node

        parent = self.getParent(self.parents[node])
        self.parents[node] = parent
        return parent

    def setParent(self, node1, node2, score):
        parent1 = self.getParent(node1)
        parent2 = self.getParent(node2)

        count1 = self.count[parent1]
        count2 = self.count[parent2]

        if count1 >= count2:
            self.parents[parent2] = parent1
            self.count[parent1] += count2
            self.scores[parent1] = min(self.scores[parent1], self.scores[parent2], score)
        else:
            self.parents[parent1] = parent2
            self.count[parent2] += count1
            self.scores[parent2] = min(self.scores[parent1], self.scores[parent2], score)
            
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dsu = DSU(n+2)
        
        for start, end, score in roads:
            dsu.setParent(start, end, score)

        p = dsu.getParent(1)
            
        return dsu.scores[p]
        
        
def test():
    params = [
        {
            "input": [
                4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
            ],
            "output": 5,
        },
        {
            "input": [
                4, [[1,2,2],[1,3,4],[3,4,7]]
            ],
            "output": 2,
        },
    ]
    solution = Solution()

    for param in params:
        n, roads = param["input"]
        result = solution.minScore(n, roads)
        print(
            "SUCCESS" if result == param["output"] else "ERROR",
            "input",
            param["input"],
            "output",
            param["output"],
            "result",
            result,
            "\n",
        )


if __name__ == "__main__":
    test()
