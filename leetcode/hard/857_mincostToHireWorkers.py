import heapq
import json
from collections import deque
from typing import List


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        N = len(quality)
        workers = [[quality[i], wage[i], (wage[i] / quality[i])] for i in range(N)]
        workers.sort(key=lambda x: x[2])

        print(workers)

        workersList = []
        proportions = []
        totalQual = 0
        res = float("inf")

        for worker in workers:
            q, p, prop = worker
            proportions.append(prop)

            totalQual += q
            heapq.heappush(workersList, (-q, -p, -prop))

            while len(workersList) > k:
                _q, _p, _prop = heapq.heappop(workersList)
                _q, _p, _prop = -_q, -_p, -_prop
                totalQual -= _q
                if _prop == proportions[-1]:
                    proportions.pop()

            if len(workersList) == k:
                curr = totalQual * proportions[-1]
                res = min(res, curr)

        return res


"""


I do not see nothing about ratio. I understand if first quality is 5 and second is 10 is should pay first*2 price.
But I do not understand this example at all:
Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667


"""


def test():
    params = [
        {
            "input": [[10, 20, 5], [70, 50, 30], 2],
            "output": 105.00000,
        },
        {
            "input": [[3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3],
            "output": 30.66667,
        },
    ]

    solution = Solution()

    for param in params:
        quality, wage, k = param["input"]
        result = solution.mincostToHireWorkers(quality, wage, k)
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
