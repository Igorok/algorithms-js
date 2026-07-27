import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution_0:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        sum4 = {}
        for num in nums4:
            sum4[num] = sum4.get(num, 0) + 1

        sum3 = {}
        for num in nums3:
            for n in sum4:
                s = num + n
                sum3[s] = sum3.get(s, 0) + sum4[n]

        sum2 = {}
        for num in nums2:
            for n in sum3:
                s = num + n
                sum2[s] = sum2.get(s, 0) + sum3[n]

        sum1 = {}
        for num in nums1:
            # x + num = 0
            # x = 0 - num
            if -num in sum2:
                sum1[0] = sum1.get(0, 0) + sum2[-num]

        return sum1.get(0, 0)


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        rightSum = {}
        for n3 in nums3:
            for n4 in nums4:
                s = n3 + n4
                rightSum[s] = rightSum.get(s, 0) + 1

        leftSum = {}
        for n1 in nums1:
            for n2 in nums2:
                s = n1 + n2
                leftSum[s] = leftSum.get(s, 0) + 1

        res = 0

        for leftVal, leftCnt in leftSum.items():
            if -leftVal not in rightSum:
                continue
            res += leftCnt * rightSum[-leftVal]

        return res


def test():
    params = [
        {
            "input": [[1, 2], [-2, -1], [-1, 2], [0, 2]],
            "output": 2,
        },
        {
            "input": [[0], [0], [0], [0]],
            "output": 1,
        },
        {
            "input": [[-1, -1], [-1, 1], [-1, 1], [1, -1]],
            "output": 6,
        },
    ]
    solution = Solution()

    for param in params:
        nums1, nums2, nums3, nums4 = param["input"]
        result = solution.fourSumCount(nums1, nums2, nums3, nums4)

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
