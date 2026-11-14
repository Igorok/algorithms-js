import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        M = len(queries)
        res = [0]*M
        _queries = sorted(
            [(n, i) for i, n in enumerate(queries)],
            key = lambda arr: arr[0]
        )

        N = len(logs)
        logs.sort(key = lambda x: x[1])

        left = -1
        right = -1
        memo = {}
        for end, id in _queries:
            while right+1 < N and logs[right+1][1] <= end:
                s, t = logs[right+1]
                memo[s] = memo.get(s, 0) + 1
                right += 1

            while left+1 < N and logs[left+1][1] < end-x:
                s, t = logs[left+1]
                memo[s] -= 1
                if memo[s] == 0:
                    del memo[s]
                left += 1

            cnt = len(memo)
            res[id] = n - cnt

        return res

def test():
    params = [
        {
            "input": [3, [[1,3],[2,6],[1,5]], 5, [10,11]],
            "output": [1,2],
        },
        {
            "input": [3, [[2,4],[2,1],[1,2],[3,1]], 2, [3,4]],
            "output": [0,1],
        },
    ]
    solution = Solution()

    for param in params:
        n, logs, x, queries = param["input"]
        result = solution.countServers(n, logs, x, queries)
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
