import heapq
import math
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from operator import countOf
from typing import List

"""
1) 1-2; 1-3; 2-4; 3-4
I have visited 4 already, so I can remove 3-4?

2) 1-2; 2-3; 3-4; 4-1;
I have already visited a 1; so I can remove a 4-1?

3) 1-2; 2-3; 3-4; 4-2;
I have already visited a 2 so I can remove a 4-2?

Look like it is a bfs only?


{
    "input": [[3, 4], [4, 1], [1, 2], [2, 3], [5, 1]],
    "output": [4, 1],
},
okay 4-1 and 5-1 and 2-3
so we have 1 node with two parents and 1 loop
it is no contradictions with description?


"""


class DSU:
    def __init__(self):
        self.parents = {}
        self.count = {}

    def get_parents(self, node):
        if node not in self.parents:
            self.parents[node] = node
            self.count[node] = 1
            return node

        parent = self.parents[node]
        if node == parent:
            return node

        p = self.get_parents(parent)
        self.parents[node] = p
        return p

    def set_parents(self, node1, node2):
        parent1 = self.get_parents(node1)
        parent2 = self.get_parents(node2)

        if parent1 == parent2:
            return

        if self.count[parent1] >= self.count[parent2]:
            self.count[parent1] += self.count[parent2]
            self.parents[parent2] = parent1
        else:
            self.count[parent2] += self.count[parent1]
            self.parents[parent1] = parent2


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        twoParentNode = None
        ans1 = None
        ans2 = None

        parents_count = defaultdict(list)
        dsu = DSU()

        N = len(edges)
        for i in range(N):
            s, e = edges[i]

            parents_count[e].append(s)
            if len(parents_count[e]) == 2:
                twoParentNode = True
                ans1 = [parents_count[e][0], e]
                ans2 = [parents_count[e][1], e]

        for i in range(N):
            s, e = edges[i]

            parent1 = dsu.get_parents(s)
            parent2 = dsu.get_parents(e)

            if parent1 == parent2 and twoParentNode == None:
                return [s, e]

            if twoParentNode != None and s == ans2[0] and e == ans2[1]:
                continue

            dsu.set_parents(s, e)

        if (
            dsu.get_parents(ans1[0])
            == dsu.get_parents(ans1[1])
            == dsu.get_parents(ans2[0])
            == dsu.get_parents(ans2[1])
        ):
            return ans2

        return ans1


def test():
    params = [
        {
            "input": [[1, 2], [1, 3], [2, 3]],
            "output": [2, 3],
        },
        {
            "input": [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]],
            "output": [4, 1],
        },
        {
            "input": [[3, 4], [4, 1], [1, 2], [2, 3], [5, 1]],
            "output": [4, 1],
        },
    ]
    solution = Solution()

    for param in params:
        edges = param["input"]
        result = solution.findRedundantDirectedConnection(edges)
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
