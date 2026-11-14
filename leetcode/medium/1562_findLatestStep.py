import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Dus:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        self.count = [1]*(n+1)

    def getParent(self, node):
        if self.parents[node] == node:
            return node

        parent = self.getParent(self.parents[node])
        self.parents[node] = parent
        return parent

    def setParent(self, node1, node2):
        parent1 = self.parents[node1]
        count1 = self.count[parent1]
        parent2 = self.parents[node2]
        count2 = self.count[parent2]

        if parent1 == parent2:
            return parent1

        if count1 >= count2:
            self.parents[parent2] = parent1
            self.count[parent1] += count2
            return parent1

        self.parents[parent1] = parent2
        self.count[parent2] += count1
        return parent2


class Solution:
    def findLatestStep(self, arr: list[int], m: int) -> int:
        N = len(arr)
        data = [0] * (N+1)
        dus = Dus(N+1)
        goodNodes = set()
        res = -1

        def checkNode(node):
            p = dus.getParent(node)
            if dus.count[p] == m and p in goodNodes:
                goodNodes.remove(p)

        for i in range(N):
            num = arr[i]
            data[num] = 1
            parent = num

            if num - 1 > 0 and data[num-1] == 1:
                checkNode(num)
                checkNode(num-1)
                parent = dus.setParent(num, num-1)

            if num + 1 < N+1 and data[num+1] == 1:
                checkNode(num)
                checkNode(num+1)
                parent = dus.setParent(num, num+1)

            cnt = dus.count[parent]
            if cnt == m:
                goodNodes.add(parent)

            if len(goodNodes) > 0:
                res = i+1

        return res


def test():
    params = [
        {
            "input": [[3,5,1,2,4], 1],
            "output": 4,
        },
        {
            "input": [[3,1,5,4,2], 2],
            "output": -1,
        },
        {
            "input": [[3,2,5,6,10,8,9,4,1,7], 3],
            "output": 9,
        },
    ]
    solution = Solution()

    for param in params:
        arr, m = param["input"]
        result = solution.findLatestStep(arr, m)
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
