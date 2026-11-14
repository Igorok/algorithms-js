import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_queue = [(weight, i) for i, weight in enumerate(servers)]
        busy_queue = []
        heapq.heapify(free_queue)

        def workProcess(t):
            while busy_queue and busy_queue[0][0] <= t:
                _t, _w, _i = heapq.heappop(busy_queue)
                heapq.heappush(free_queue, (_w, _i))

        N = len(tasks)
        curr = 0
        res = []
        for t in range(N):
            curr = max(curr, t)
            workProcess(curr)

            if not free_queue:
                curr = busy_queue[0][0]
                workProcess(curr)

            task = tasks[t]
            _w, _i = heapq.heappop(free_queue)

            res.append(_i)
            heapq.heappush(busy_queue, (curr+task, _w, _i))


        return res

'''
{
    "input": [[3,3,2], [1,2,3,2,1,2]],
    "output": [2,2,0,2,1,2],
},

    0 1 2 3 4 5
    1,2,3,2,1,2
3   0   5
3   0
2   0 1 3 5



'''

def test():
    params = [
        {
            "input": [[3,3,2], [1,2,3,2,1,2]],
            "output": [2,2,0,2,1,2],
        },
        {
            "input": [[5,1,4,3,2], [2,1,2,4,5,2,1]],
            "output": [1,4,1,4,1,3,2],
        },
        {
            "input": [
                [10,63,95,16,85,57,83,95,6,29,71],
                [70,31,83,15,32,67,98,65,56,48,38,90,5],
            ],
            "output": [8,0,3,9,5,1,10,6,4,2,7,9,0],
        },
    ]
    solution = Solution()

    for param in params:
        servers, tasks = param["input"]
        result = solution.assignTasks(servers, tasks)
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
