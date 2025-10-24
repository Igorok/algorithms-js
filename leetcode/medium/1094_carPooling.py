from typing import List
import json
from collections import deque, defaultdict
from functools import lru_cache
import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        data = [0] * (1+10**5)

        for cnt, left, right in trips:
            data[left] += cnt
            data[right] -= cnt

        acc = 0
        for i in range(1+10**5):
            acc += data[i]
            if acc > capacity:
                return False

        return True




def test():
    params = [
        {
            "input": [[[2,1,5],[3,3,7]], 4],
            "output": False,
        },
        {
            "input": [[[2,1,5],[3,3,7]], 5],
            "output": True,
        },
    ]
    solution = Solution()

    for param in params:
        trips, capacity = param["input"]
        result = solution.carPooling(trips, capacity)
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
