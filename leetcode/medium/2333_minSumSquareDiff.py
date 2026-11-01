import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution_0:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        N = len(nums1)
        data = [
            ((nums1[i] - nums2[i])**2, nums1[i], nums2[i]) for i in range(N)
        ]
        data.sort(key=lambda x: -1 * x[0])

        print('data', data)

        available = k1 + k2
        res = 0
        for i in range(N):
            _, n1, n2 = data[i]
            diff = abs(n1 - n2)
            num = min(diff, available)
            diff -= num
            available -= num
            res += diff ** 2




        return res

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        countOfDiff = defaultdict(int)
        countOfDiff[0] = 0
        for n1, n2 in zip(nums1, nums2):
            countOfDiff[abs(n1-n2)] += 1

        countOfDiff = sorted(countOfDiff.items(), key=lambda x: -x[0])

        # print(countOfDiff)

        N = len(countOfDiff)
        acc = k1+k2
        res = 0

        for i in range(N):
            curr, cnt = countOfDiff[i]
            if curr == 0:
                break

            if acc == 0:
                res += (curr ** 2) * cnt
                continue

            nextDiff = countOfDiff[i+1][0]
            diff = curr - nextDiff
            toRemove = diff * cnt
            if toRemove < acc:
                acc -= toRemove
                countOfDiff[i+1] = [
                    countOfDiff[i+1][0],
                    countOfDiff[i+1][1] + cnt
                ]
                continue

            # after removing
            curr = curr - (acc // cnt)
            acc = acc % cnt

            res += ((curr-1) ** 2) * acc
            res += (curr ** 2) * (cnt - acc)

            acc = 0


        return res


def test():
    params = [
        {
            "input": [[1,2,3,4], [2,10,20,19], 0, 0],
            "output": 579,
        },
        {
            "input": [[1,4,10,12], [5,8,6,9], 1, 1],
            "output": 43,
        },
    ]
    solution = Solution()

    for param in params:
        nums1, nums2, k1, k2 = param["input"]
        result = solution.minSumSquareDiff(nums1, nums2, k1, k2)

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
