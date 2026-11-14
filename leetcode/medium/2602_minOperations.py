import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()
        prefix = [0] * N
        prefix[0] = nums[0]
        for i in range(1, N):
            prefix[i] = prefix[i-1] + nums[i]

        # print('prefix', prefix)

        def getSum(val):
            start = 0
            end = N-1
            id = -1
            while start <= end:
                m = (start + end) // 2
                if nums[m] <= val:
                    id = m
                    start = m + 1
                else:
                    end = m - 1

            wantLeft = 0 if id == -1 else (id+1)*val
            diffLeft = 0 if id == -1 else wantLeft - prefix[id]

            wantRight = 0 if id == N-1 else (N-id-1)*val
            leftSum = 0 if id == -1 else prefix[id]
            diffRight = 0 if id == N-1 else prefix[-1] - leftSum - wantRight

            # print(
            #     'id', id,
            #     'diffLeft', diffLeft,
            #     'diffRight', diffRight,
            # )

            return diffLeft + diffRight

        M = len(queries)
        res = [0] * M
        for i in range(M):
            res[i] = getSum(queries[i])

        return res

def test():
    params = [
        {
            "input": [[3,1,6,8], [1,5]],
            "output": [14,10],
        },
        {
            "input": [[2,9,6,3], [10]],
            "output": [20],
        },
        {
            "input": [[5], [6,5,3,1]],
            "output": [1,0,2,4],
        },
    ]
    solution = Solution()

    for param in params:
        nums, queries = param["input"]
        result = solution.minOperations(nums, queries)
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
