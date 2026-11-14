import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List

class Solution_0:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        N = len(nums1)
        M = len(nums2)

        prev = [0]*M
        for i in range(N):
            curr = [0]*M
            for j in range(M):
                top = 0 if i == 0 else prev[j]
                left = 0 if j == 0 else curr[j-1]
                curr[j] = max(top, left)

                if nums1[i] == nums2[j]:
                    diag = 0 if i == 0 or j == 0 else prev[j-1]
                    curr[j] = max(curr[j], diag+1)



            prev = curr

        # print(prev)


        return prev[-1]

'''
- 1 2 3 2 1
3 0 0 1 1 1
2 0 1 1 2 2
1 1 1 1 1 3
4 1
7


- 0,1,1,1,1
1 0 1 1 1 1
0 1 1 1 1 1
1 1 2 2 2 2
0 1 2 2 2 2
1 1 2 3 3 3

'''


class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        N = len(nums1)
        M = len(nums2)

        res = 0

        prev = [0]*M
        for i in range(N):
            curr = [0]*M
            for j in range(M):
                if nums1[i] == nums2[j]:
                    diag = 0 if i == 0 or j == 0 else prev[j-1]
                    curr[j] = max(curr[j], diag+1)
                else:
                    curr[j] = 0


                res = max(curr[j], res)

            prev = curr


        return res

def test():
    params = [
        {
            "input": [[1,2,3,2,1], [3,2,1,4,7]],
            "output": 3,
        },
        {
            "input": [[0,0,0,0,0], [0,0,0,0,0]],
            "output": 5,
        },
        {
            "input": [[0,1,1,1,1], [1,0,1,0,1]],
            "output": 2,
        },
    ]
    solution = Solution()

    for param in params:
        nums1, nums2 = param["input"]
        result = solution.findLength(nums1, nums2)
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
