from typing import List
import json
from collections import deque, defaultdict
from functools import lru_cache
import heapq


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        pLength = len(people)
        peopleData = [(people[i], i) for i in range(pLength)]
        peopleData.sort()

        res = [0] * pLength
        flId = 0
        flLength = len(flowers)
        flQueue = []
        for dt, id in peopleData:
            while flId < flLength and flowers[flId][0] <= dt:
                s, e = flowers[flId]
                heapq.heappush(flQueue, (e, s))
                flId += 1

            while flQueue and flQueue[0][0] < dt:
                heapq.heappop(flQueue)

            res[id] = len(flQueue)

        return res



def test():
    params = [
        {
            "input": [[[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]],
            "output": [1,2,2,2],
        },
        {
            "input": [[[1,10],[3,3]], [3,3,2]],
            "output": [2,2,1],
        },
    ]
    solution = Solution()

    for param in params:
        flowers, people = param["input"]
        result = solution.fullBloomFlowers(flowers, people)
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
