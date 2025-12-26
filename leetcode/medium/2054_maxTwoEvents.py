import json
from collections import defaultdict, deque
from typing import List
import heapq

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort()
        maxEventsVal = [-1] * N
        maxEventsVal[N-1] = events[N-1][2]

        for i in range(N-2, -1, -1):
            maxEventsVal[i] = max(maxEventsVal[i+1], events[i][2])

        def getMaxVal(id, end):
            left = id
            right = N-1

            res = -1
            while left <= right:
                middle = (left + right) // 2

                if events[middle][0] > end:
                    res = middle
                    right = middle - 1
                else:
                    left = middle + 1

            return 0 if res == -1 else maxEventsVal[res]


        res = 0
        for i in range(N):
            s, e, v = events[i]
            r = v + getMaxVal(i, e)
            res = max(res, r)


        return res


def test():
    params = [
        {
            "input": [[1,3,2],[4,5,2],[2,4,3]],
            "output": 4,
        },
        {
            "input": [[1,3,2],[4,5,2],[1,5,5]],
            "output": 5,
        },
        {
            "input": [[1,5,3],[1,5,1],[6,6,5]],
            "output": 8,
        },
    ]
    solution = Solution()

    for param in params:
        events = param["input"]
        result = solution.maxTwoEvents(events)
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
