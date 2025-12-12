from typing import List
import json
from collections import deque, defaultdict, Counter
import heapq
import math
from functools import cache


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        delay = [-1]*(n+1)
        adj = [[] for i in range(n+1)]

        for s, e, t in times:
            adj[s].append((e, t))

        queue = [(k, 0)]
        visited = 1
        delay[k] = 0

        while queue:
            node, curr = heapq.heappop(queue)

            for nei, t in adj[node]:
                if delay[nei] == -1:
                    visited += 1
                newT = curr + t
                if delay[nei] == -1 or delay[nei] > newT:
                    delay[nei] = newT
                    heapq.heappush(queue, (nei, newT))


        return -1 if visited != n else max(delay)



def test ():
    params = [
        {
            'input': [[[2,1,1],[2,3,1],[3,4,1]], 4, 2],
            'output': 2,
        },
        {
            'input': [[[1,2,1]], 2, 1],
            'output': 1,
        },
        {
            'input': [[[1,2,1]], 2, 2],
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        times, n, k  = param['input']
        result = solution.networkDelayTime(times, n, k)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            # msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
