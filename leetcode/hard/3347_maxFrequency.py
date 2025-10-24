from typing import List
import json
from collections import deque, defaultdict
from functools import lru_cache
import heapq

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        points = set()
        countOfPoints = defaultdict(int)
        sweepOfIntervals = defaultdict(int)

        for num in nums:
            countOfPoints[num] += 1
            start = num - k
            end = num + k + 1
            sweepOfIntervals[start] += 1
            sweepOfIntervals[end] -= 1
            points.update([start, num, end])

        res = 1
        acc = 0
        for point in sorted(list(points)):
            acc += sweepOfIntervals[point]

            availableOperations = min(numOperations, acc - countOfPoints[point])
            realOperations = countOfPoints[point] + availableOperations
            res = max(res, realOperations)

        return res

'''
nums = [1, 4, 8, 13], k = 5, and numOperations = 2.
points = [-4, 1, 6, -1, 4, 9, 3, 8, 13, 18]
points = [-4, -1, 1, 3, 4, 6, 8, 9, 13, 18]

sweep line
-4, -1, 1, 3, 4, 6, 8, 9, 13, 18
1    1     1     -1 1 -1  -1  -1
1    2     3     2  3  2   1   0

cnt_points - кол-во реальных точек

for point in sorted(points):
    points_cover_this_point += points_cover[point]
    res = max(res, cnt_points[point] +
                min(points_cover_this_point - cnt_points[point], numOperations))

доступно для операции = min(кол-во вхождений интервалов - кол-во точек, лимит операций)
available = min(points_cover_this_point - cnt_points[point], numOperations))

ответ кол-во реальных точек с 0 операций + мин доступное кол-во операций
res = max(res, cnt_points[point] + available)


'''



def test():
    params = [
        {
            "input": [[1,4,5], 1, 2],
            "output": 2,
        },
        {
            "input": [[5,11,20,20], 5, 1],
            "output": 2,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k, numOperations = param["input"]
        result = solution.maxFrequency(nums, k, numOperations)
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
