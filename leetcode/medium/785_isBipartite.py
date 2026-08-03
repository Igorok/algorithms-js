from collections import deque
from json import dumps
from typing import List


class DSU:
    def __init__(self):
        self.parents = {}
        self.count = {}

    def getParent(self, n):
        if n not in self.parents:
            self.parents[n] = n
            self.count[n] = 1
            return n

        if self.parents[n] == n:
            return n

        p = self.getParent(self.parents[n])
        self.parents[n] = p
        return p

    def setParent(self, n1, n2):
        p1 = self.getParent(n1)
        cnt1 = self.count[p1]

        p2 = self.getParent(n2)
        cnt2 = self.count[p2]

        if p1 == p2:
            return

        if cnt1 >= cnt2:
            self.parents[p2] = p1
            self.count[p1] += cnt2
        else:
            self.parents[p1] = p2
            self.count[p2] += cnt1


class Solution_0:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        dsu = DSU()
        last = -1

        for arr in graph:
            for i in range(len(arr)):
                p = arr[0]
                n = arr[i]
                dsu.setParent(p, n)
                last = max(last, arr[i])

        parents = set()
        for node in dsu.parents:
            p = dsu.getParent(node)
            parents.add(p)
            # if len(parents) > 2:
            #     return False

        return len(parents) > 1


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        length = len(graph)
        colors = [-1] * length

        def dfs(node):
            for nei in graph[node]:
                if colors[nei] == -1:
                    colors[nei] = (colors[node] + 1) % 2
                    r = dfs(nei)
                    if not r:
                        return False
                    continue

                if colors[node] == colors[nei]:
                    return False

            return True

        for node in range(length):
            if colors[node] == -1:
                colors[node] = 0

            r = dfs(node)
            if not r:
                return False

        return True


"""

A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

It means:
    [[1,2,3],[0,2],[0,1,3],[0,2]]
    [1,2,3] - 0 is A set and 1,2,3 is a B set?
    [0,2] - 1 - B sent and 0,2 is a B set?


"""


def test():
    params = [
        {
            "input": [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]],
            "output": False,
        },
        {
            "input": [[1, 3], [0, 2], [1, 3], [0, 2]],
            "output": True,
        },
        {
            "input": [[4, 1], [0, 2], [1, 3], [2, 4], [3, 0]],
            "output": False,
        },
        {
            "input": [[1], [0], [4], [4], [2, 3]],
            "output": True,
        },
    ]
    solution = Solution()

    for param in params:
        graph = param["input"]
        result = solution.isBipartite(graph)
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
