import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        def convert(num, id):
            n = num
            res = 0
            while n > 0:
                res += n % 10
                n = n // 10
            return (res, num, id)

        data = [convert(nums[i], i) for i in range(N)]
        data.sort()
        # print(data)

        visited = [0]*N

        def dfs(id, length):
            visited[id] = 1
            nextId = data[id][2]

            if visited[nextId] == 1:
                return length + 1

            return dfs(nextId, length + 1)

        res = 0
        for i in range(N):
            if i != data[i][2] and visited[i] != 1:
                length = dfs(i, 0)
                res += length - 1


        return res


def test():
    params = [
        {
            "input": [37,100],
            "output": 1,
        },
        {
            "input": [22,14,33,7],
            "output": 0,
        },
        {
            "input":  [18,43,34,16],
            "output": 2,
        },
        {
            "input": [268835996,65052660,415128775],
            "output": 2,
        },


    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.minSwaps(nums)

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
