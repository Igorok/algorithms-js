from typing import List
import json
from collections import deque, defaultdict
from sortedcontainers import SortedList
import heapq


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parents = [i for i in range(c+1)]
        counts = [1]*(c+1)
        statuses = [1]*(c+1)
        nodes = [[] for i in range(c+1)]

        def getParent(node):
            if parents[node] == node:
                return node

            parent = parents[node]
            grand = getParent(parent)

            if parent == grand:
                return parent

            parents[node] = grand

            return grand

        def setParent(node1, node2):
            parent1 = getParent(node1)
            parent2 = getParent(node2)

            if counts[parent1] >= counts[parent2]:
                parents[parent2] = parent1
                counts[parent1] += counts[parent2]
            else:
                parents[parent1] = parent2
                counts[parent2] += counts[parent1]

        for s, e in connections:
            setParent(s, e)

        for node in range(c+1):
            parent = getParent(node)
            heapq.heappush(nodes[parent], node)


        res = []
        for command, node in queries:
            if command == 2:
                statuses[node] = 0
                continue

            if statuses[node] == 1:
                res.append(node)
                continue

            parent = getParent(node)
            while len(nodes[parent]) > 0 and statuses[nodes[parent][0]] == 0:
                heapq.heappop(nodes[parent])

            res.append(-1 if len(nodes[parent]) == 0 else nodes[parent][0])

        return res

def test ():
    params = [
        {
            'input': [5, [[1,2],[2,3],[3,4],[4,5]], [[1,3],[2,1],[1,1],[2,2],[1,2]]],
            'output': [3,2,3],
        },
        {
            'input': [3, [], [[1,1],[2,1],[1,1]]],
            'output': [1,-1],
        },
    ]
    solution = Solution()

    for param in params:
        c, connections, queries = param['input']
        result = solution.processQueries(c, connections, queries)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
