import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        stopByBus = {}
        busByStop = {}

        for bus in range(len(routes)):
            stopByBus[bus] = set(routes[bus])

            for rout in routes[bus]:
                if rout not in busByStop:
                    busByStop[rout] = []
                busByStop[rout].append(bus)

        visitedBus = set()
        visitedStop = set()

        busQueue = deque()

        if source not in busByStop:
            return -1

        for bus in busByStop[source]:
            visitedBus.add(bus)
            visitedStop.add(source)

            busQueue.append((bus, 1))

        while busQueue:
            bus, cnt = busQueue.popleft()

            if target in stopByBus[bus]:
                return cnt

            for stop in stopByBus[bus]:
                if stop in visitedStop:
                    continue
                for newBus in busByStop[stop]:
                    if newBus in visitedBus:
                        continue

                    visitedStop.add(stop)
                    visitedBus.add(newBus)

                    busQueue.append((newBus, cnt + 1))

        return -1


def test():
    params = [
        {
            "input": [[[1, 2, 7], [3, 6, 7]], 1, 6],
            "output": 2,
        },
        {
            "input": [[[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12],
            "output": -1,
        },
        {
            "input": [[[1, 2, 7], [3, 6, 7]], 8, 6],
            "output": -1,
        },
    ]
    solution = Solution()

    for param in params:
        routes, source, target = param["input"]
        result = solution.numBusesToDestination(routes, source, target)

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
