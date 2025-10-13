from typing import List
import json
from collections import deque, defaultdict


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        countOfVal = {}
        for num in power:
            countOfVal[num] = countOfVal.get(num, 0) + 1

        nums = list(countOfVal.keys())
        nums.sort()
        n = len(nums)

        cache = {}

        def dfs(id):
            if id in cache:
                return cache[id]

            if id >= n:
                return 0

            val = nums[id]
            res = val * countOfVal[val]

            nextId = id + 1
            while nextId < n and nums[nextId] < val + 3:
                nextId += 1

            r = dfs(nextId)
            if nextId + 1 < n and nums[nextId + 1] < nums[nextId] + 3:
                r1 = dfs(nextId + 1)
                r = max(r, r1)
            if nextId + 2 < n and nums[nextId + 2] < nums[nextId] + 3:
                r1 = dfs(nextId + 2)
                r = max(r, r1)

            cache[id] = res + r
            return cache[id]


        r = dfs(0)
        if (n > 1):
            r1 = dfs(1)
            r = max(r, r1)
        if n > 2:
            r2 = dfs(2)
            r = max(r, r2)

        return r

'''
1 2 3 4 5 6 7 8 9

'''



def test():
    params = [
        {
            "input": [1,1,3,4],
            "output": 6,
        },
        {
            "input": [7,1,6,6],
            "output": 13,
        },
    ]
    solution = Solution()

    for param in params:
        power = param["input"]
        result = solution.maximumTotalDamage(power)
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
