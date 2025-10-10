from typing import List
from json import dumps
from collections import defaultdict, deque
import heapq


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        m = len(worker)
        jobs = [[difficulty[i], profit[i]] for i in range(n)]
        jobs.sort(key=lambda x: x[0])
        maxProfit = -1
        for i in range(n):
            maxProfit = max(maxProfit, jobs[i][1])
            jobs[i].append(maxProfit)

        def getProfit(ability):
            start = 0
            end = n-1
            id = -1

            while start <= end:
                middle = (start + end) // 2
                if jobs[middle][0] <= ability:
                    id = middle
                    start = middle + 1
                else:
                    end = middle - 1

            return 0 if id == -1 else jobs[id][2]

        res = 0
        for ability in worker:
            res += getProfit(ability)

        return res


def test ():
    params = [
        {
            'input': [[2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]],
            'output': 100,
        },
        {
            'input': [[85,47,57], [24,66,99], [40,25,25]],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        difficulty, profit, worker = param['input']
        result = solution.maxProfitAssignment(difficulty, profit, worker)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
